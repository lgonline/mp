#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/4 16:42
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : useICMPToPing.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com
# @Description: 通过ICMP查验网络中的主机
#   
#   

import os
import argparse
import socket
import struct
import select
import time

ICMP_ECHO_REQUEST = 8
DEFAULT__TIMEOUT = 2
DEFAULT_COUNT = 4

class Pinger(object):
    def __init__(self,target_host,count=DEFAULT_COUNT,timeout=DEFAULT__TIMEOUT):
        self.target_host = target_host
        self.count = count
        self.timeout = timeout

    def do_check(self,source_string):
        sum = 0
        max_count = (len(source_string))*2
        count = 0
        while count < max_count:
            #ord()函数是chr()或unichr()函数的配对函数，以一个字符作为参数，返回对应的ASCII数值，或者Unicode数值
            val = ord(source_string[count+1])*256 + ord(source_string[count])
            sum = sum + val
            sum = sum & 0xffffffff
            count = count + 2

        if max_count < len(source_string):
            sum = sum + ord(source_string[len(source_string) - 1])
            sum = sum & 0xffffffff
            count = count + 2

        sum = (sum >> 16) + (sum & 0xffff)
        sum = sum + (sum >> 16)
        answer = ~sum
        answer = answer & 0xffff
        answer = answer >> 8 | (answer << 8 & 0xff00)
        return answer

    def receive_pone(self,sock,ID,timeout):
        time_remainint = timeout

        while True:
            start_time = time.time()
            readable = select.select([sock],[],[],time_remainint)
            time_spent = (time.time() - start_time)
            if readable[0] == []:
                return

            time_received = time.time()
            recv_packet,addr = sock.recvfrom(1024)
            icmp_header = recv_packet[20:28]
            type,code,checksum,packet_ID,segquence = struct.unpack("bbHHh",icmp_header)

            if packet_ID == ID:
                bytes_In_double = struct.calcsize("d")
                time_sent = struct.unpack("d",recv_packet[28:28+bytes_In_double])[0]
                return time_received - time_sent

            time_reaminint = time_remainint - time_spent

            if time_remainint <= 0:
                return

    def send_ping(self,sock,ID):
        target_addr = socket.gethostbyname(self.target_host)

        my_checksum = 0

        header = struct.pack("bbHHh",ICMP_ECHO_REQUEST,0,my_checksum,ID,1)
        bytes_In_double = struct.calcsize("d")
        data = (192 - bytes_In_double) * "Q"
        data = struct.pack("d",time.time()) + data

        my_checksum = self.do_check(header+data)
        header = struct.pack("bbHHb",ICMP_ECHO_REQUEST,0,socket.htons(my_checksum),ID,1)
        packet = header + data
        sock.sendto(packet,(target_addr,1))

    def ping_once(self):
        icmp = socket.getprotobyname("icmp")
        try:
            sock = socket.socket(socket.AF_INET,socket.SOCK_RAW,icmp)
        except socket.error as (errno,msg):
            if errno == 1:
                msg += "ICMP messages can only be sent from root user processes"
                raise socket.error(msg)
        except Exception as e:
            print("Exception: %s" % (e))

        my_ID = os.getpid() & 0xFFFF

        self.send_ping(sock,my_ID)
        delay = self.receive_pone(sock,my_ID,self.timeout)
        sock.close()
        return delay

    def ping(self):
        for i in range(self.count):
            print('pint to %s ...',self.target_host)
            try:
                delay = self.ping_once()
            except socket.gaierror as e:
                print('ping failed (socket error : %s'% e[1])
                break

            if delay == None:
                print('ping failed')
            else:
                delay = delay * 1000
                print('get pone in %0.4fms'% delay)


# def main():
#     pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Python ping')
    parser.add_argument('--target-host',action='store',desk='target_host',required=True)
    given_args = parser.parse_args()
    target_host = given_args.target_host
    pinger = Pinger(target_host=target_host)
    pinger.ping()

    # main()
    pass