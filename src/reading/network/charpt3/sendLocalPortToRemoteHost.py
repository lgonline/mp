#!/usr/bin/env python  
# -*- coding: utf-8 -*-

""" 
@version: v1.0 
@author: 330mlcc 
@Software: PyCharm
@license: Apache Licence  
@Email   : mlcc330@hotmail.com
@contact: 3323202070@qq.com
@site:  
@software: PyCharm 
@file: sendLocalPortToRemoteHost.py
@time: 18-7-1 下午2:42 
Description:
Python的asyncore模块提供了以异步的方式写入套接字服务的客户端和服务器的基础结构。

模块主要包括：

asyncore.loop(…) - 用于循环监听网络事件。loop()函数负责检测一个字典，字典中保存dispatcher的实例。

asyncore.dispatcher类 - 一个底层套接字对象的简单封装。这个类有少数由异步循环调用的，用来事件处理的函数。

dispatcher类中的writable()和readable()在检测到一个socket可以写入或者数据到达的时候被调用，并返回一个bool值，决定是否调用handle_read或者handle_write。
asyncore.dispatcher_with_send类 - 一个 dispatcher的子类，添加了简单的缓冲输出能力，对简单的客户端很有用。
"""

# PortForwarder在本地套接字种保存进入客户端的请求，然后把这个套接字传递给Sender类实例，再使用Receiver类实例发起与远程主机指定端口之间的双向通信

import argparse
import asyncore
import socket

LOCAL_SERVER_HOST = '127.0.0.1'
REMOTE_SERVER_HOST = 'www.baidu.com'
BUFSIZ = 4096

class PortForwarder(asyncore.dispatcher):       #创建一个端口转发类，继承自asyncore.dispatcher
    def __init__(self,ip,port,remoteip,remoteport,backlog=5):
        asyncore.dispatcher.__init__(self)
        self.remoteip = remoteip
        self.remoteport = remoteport
        self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((ip,port))
        self.listen(backlog)

    def handle_accept(self):
        conn,addr = self.accept()
        print('Connect to : ',addr)
        Sender(Receive(conn),self.remoteip,self.remoteport)

class Receive(asyncore.dispatcher): #处理进入的客户端请求
    def __init__(self,conn):
        asyncore.dispatcher.__init__(self.conn)
        self.from_remote_buff = ''
        self.to_remote_buffer = ''
        self.sender = None

    def handle_connect(self):
        pass

    def handle_read(self):
        read = self.recv(BUFSIZ)
        self.from_remote_buff += read

    def writable(self):
        return (len(self.to_remote_buffer) > 0)

    def handle_write(self):
        sent = self.send(self.to_remote_buffer)
        self.to_remote_buffer = self.to_remote_buffer[sent:]

    def handle_close(self):
        self.close()
        if self.sender:
            self.sender.close()

class Sender(asyncore.dispatcher):  #接收一个RECEIVE的实例，把数据发送给客户
    def __init__(self,receiver,remoteaddr,remoteport):
        asyncore.dispatcher.__init__(self)
        self.receiver = receiver
        receiver.sender = self
        self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connect((remoteaddr,remoteport))

    def handle_connect(self):
        pass

    def handle_read(self):
        read = self.recv(BUFSIZ)
        self.receiver.to_remote_buffer += read

    def writable(self):
        return (len(self.receiver.from_remote_buffer) > 0)

    def handle_write(self):
        sent = self.send(self.receiver.from_remote_buffer)
        self.receiver.frrom_remote_buffer = self.receiver.from_remote_buffer[sent:]

    def handle_close(self):
        self.close()
        self.receiver.close()
#
# def main():
#     pass


if __name__ == '__main__':
    # main()

    parser = argparse.ArgumentParser(description='Stackless Socket Server Example')
    parser.add_argument('--local-host',action='store',dest='local_host',default=LOCAL_SERVER_HOST)
    parser.add_argument('--local-port',action='store',dest='local_port',type=int,required=True)
    parser.add_argument('--remote-host',action='store',dest='remote_host',default=REMOTE_SERVER_HOST)
    parser.add_argument('--remote-port',action='store',dest='remote_port',type=int,default=80)
    given_args = parser.parse_args()
    local_host,remote_host = given_args.local_host,given_args.remote_host
    local_port,remote_port = given_args.local_port,given_args.local_port

    print('sarting port forwarding local %s:%s => remote %s:%s'% (local_host,local_port,remote_host,remote_port))
    PortForwarder(local_host,local_port,remote_host,remote_port)
    asyncore.loop()


    pass


    
    