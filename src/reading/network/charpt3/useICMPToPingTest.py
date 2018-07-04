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

    # 验证数据包的完整性,接收一个源字符串，经过处理后生成一个特殊的校验和
    def do_checksum(self,source_string):
        print 'source_string is : ',source_string
        print ('len(source_string) is : ',len(source_string) )
        sum = 0
        max_count = (len(source_string)/2)*2
        print 'max_count is : ',max_count

        count = 0
        print 'ord(source_string[count]) is : ',ord(source_string[count])
        print 'ord(source_string[count + 1] *256 is :',ord(source_string[count + 1]) * 256
        while count < max_count:
            print '-------------------------'
            print 'start count is : ',count

            #ord()函数是chr()或unichr()函数的配对函数，以一个字符作为参数，返回对应的ASCII数值，或者Unicode数值
            val = ord(source_string[count+1])*256 + ord(source_string[count])
            print 'ord(source_string[count + 1] *256 is :', ord(source_string[count + 1]) * 256
            print 'ord(source_string[count]) is : ', ord(source_string[count])
            print 'ord(source_string[count+1])*256 + ord(source_string[count]) is ',val
            sum = sum + val
            print 'sum + val is : ',sum
            sum = sum & 0xffffffff
            print 'sum & 0xffffffff is ',sum
            count = count + 2
            print 'end count is : ',count
            print '************************'

        if max_count < len(source_string):
            print '###########################'
            print ' ord(source_string[len(source_string)) is : ',ord(source_string[len(source_string)-1])
            print 'start sum is : ',sum
            sum = sum + ord(source_string[len(source_string) - 1])
            print 'sum + ord(source_string[len(source_string) - 1]) is : ',sum
            sum = sum & 0xffffffff
            print 'sum & 0xffffffff is : ',sum
            count = count + 2


        print '$$$$$$$$$$$$$$$$$$$$$$$$'
        print 'befor sum is : ',sum
        print '(sum >> 16) is ',(sum >> 16)
        print '(sum & 0xffff) is ',(sum & 0xffff)
        sum = (sum >> 16) + (sum & 0xffff)
        print '(sum >> 16) + (sum & 0xffff) is : ',sum
        sum = sum + (sum >> 16)
        print 'sum + (sum >> 16) is : ',sum
        answer = ~sum
        print 'answer = ~sum is : ',answer
        answer = answer & 0xffff
        print 'answer & 0xffff is : ',answer

        print 'answer >> 8 is : ',(answer >> 8)
        print '(answer << 8 & 0xff00) is : ',(answer << 8 & 0xff00)
        answer = answer >> 8 | (answer << 8 & 0xff00)
        print 'answer >> 8 | (answer << 8 & 0xff00) is : ',answer
        return answer
        # print answer

    # 从socket中接收ping，在未达到超时时间之前一直等待响应，或者直接接收响应，然后抓取ICMP响应首部
    #
    def receive_pone(self,sock,ID,timeout):
        print '---------------start receive_pone()---------------------'
        time_remainint = timeout
        print 'timeout is : ',timeout

        while True:
            start_time = time.time()
            print '1 start_time is : ',start_time
            '''
            Python的select()方法直接调用操作系统的IO接口，
            它监控sockets,open files, and pipes(所有带fileno()方法的文件句柄)何时变成readable 和writeable, 或者通信错误，
            select()使得同时监控多个连接变的简单，并且这比写一个长循环来等待和监控多客户端连接要高效，
            因为select直接通过操作系统提供的C的网络接口进行操作，而不是通过Python的解释器。
            '''
            readable = select.select([sock],[],[],time_remainint)
            print 'select.select([sock],[],[],time_remainint) is : ',readable
            time_spent = (time.time() - start_time)
            print '(time.time() - start_time) is : ',time_spent
            if readable[0] == []:   #Timeout
                return

            time_received = time.time()
            print 'time_received is : ',time_received
            recv_packet,addr = sock.recvfrom(1024)
            print 'recv_packet,addr is : ',sock.recvfrom(1024)
            icmp_header = recv_packet[20:28]
            print 'recv_packet[20:28] is : ',recv_packet[20:28]
            type,code,checksum,packet_ID,segquence = struct.unpack("bbHHh",icmp_header)
            print 'type,code,checksum,packet_ID,segquence is : ',struct.unpack("bbHHh",icmp_header)
            print 'type is : ',type
            print 'code is : ',code
            print 'checksum is : ',checksum
            print 'packet_ID is : ',packet_ID

            if packet_ID == ID:
                bytes_In_double = struct.calcsize("d")
                time_sent = struct.unpack("d",recv_packet[28:28+bytes_In_double])[0]
                return time_received - time_sent

            time_reaminint = time_remainint - time_spent

            if time_remainint <= 0:
                return

        print '---------------end receive_pone()---------------------'

    # 获取目标主机的DNS主机名
    def send_ping(self,sock,ID):
        print '-------------start send_ping()------------------'
        target_addr = socket.gethostbyname(self.target_host)
        print 'self.target_host is : ',self.target_host
        print 'socket.gethostbyname(self.target_host) is : ',socket.gethostbyname(self.target_host)

        my_checksum = 0
        # 使用struct方法创建一个ICMP_ECHO_REQUEST数据包
        # struct.pack用于将Python的值根据格式符，转换为字符串（因为Python中没有字节(Byte)类型，可以把这里的字符串理解为字节流，或字节数组）
        header = struct.pack("bbHHh",ICMP_ECHO_REQUEST,0,my_checksum,ID,1)
        print '1 header(struct.pack("bbHHh",ICMP_ECHO_REQUEST,0,my_checksum,ID,1)) is : ',struct.pack("bbHHh",ICMP_ECHO_REQUEST,0,my_checksum,ID,1)
        # 计算给定的格式(fmt)占用多少字节的内存,d为double
        bytes_In_double = struct.calcsize("d")
        print 'struct.calcsize("d") is : ',struct.calcsize("d")
        data = (192 - bytes_In_double) * "Q"
        print '(192 - bytes_In_double) * "Q" is : ',(192 - bytes_In_double) * "Q"
        data = struct.pack("d",time.time()) + data
        print 'struct.pack("d",time.time()) + data is : ',data

        my_checksum = self.do_checksum(header+data)
        print 'my_checksum is : ',my_checksum
        header = struct.pack("bbHHb",ICMP_ECHO_REQUEST,0,socket.htons(my_checksum),ID,1)
        print '2 header = struct.pack("bbHHb",ICMP_ECHO_REQUEST,0,socket.htons(my_checksum),ID,1) is ',header
        packet = header + data
        print 'header + data is : ',packet
        sock.sendto(packet,(target_addr,1))
        print 'sock.sendto(packet,(target_addr,1)) is : ',sock.sendto(packet,(target_addr,1))
        print '------------------end send_pint()-----------------'

    def ping_once(self):
        print '----------start ping_once--------------'
        icmp = socket.getprotobyname("icmp")
        print 'icmp is : ',icmp
        try:
            sock = socket.socket(socket.AF_INET,socket.SOCK_RAW,icmp)
        except socket.error,(errno,msg):
            if errno == 1:
                msg += "ICMP messages can only be sent from root user processes"
                raise socket.error(msg)
        except Exception,e:
            print "Exception: %s" % (e)

        print 'os.getpid() is : ',os.getpid()
        my_ID = os.getpid() & 0xFFFF
        print 'os.getpid() & 0xFFFF is : ',my_ID

        self.send_ping(sock,my_ID)
        delay = self.receive_pone(sock,my_ID,self.timeout)
        print 'delay is : ',delay
        sock.close()
        return delay
        print '-------------end ping_once---------------'

    def ping(self):
        '''
        xrange 用法与 range 完全相同，所不同的是生成的不是一个list对象，而是一个生成器。
        要生成很大的数字序列的时候，用xrange会比range性能优很多，因为不需要一上来就开辟一块很大的内存空间。
        '''
        for i in xrange(self.count):
            print 'pint to %s ...',self.target_host
            try:
                delay = self.ping_once()
            except socket.gaierror as e:
                print 'ping failed (socket error : %s'% e[1]
                break

            if delay == None:
                print 'ping failed'
            else:
                delay = delay * 1000
                print 'get pone in %0.4fms'% delay

# def main():
#     pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Python ping')
    parser.add_argument('--target-host',action='store',desk='target_host',required=True)
    given_args = parser.parse_args()
    target_host = given_args.target_host
    pinger = Pinger(target_host=target_host)
    pinger.ping()

    # pinger = Pinger('www.jd.com')
    # pinger.ping()
    # pinger.do_check('www.jd.com')

    # main()
    pass