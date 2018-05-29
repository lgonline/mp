#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: 330mlcc 
@license: Apache Licence  
@contact: lg_online@126.com 
@site:  
@software: PyCharm 
@file: MyTimestampClient
@time: 18-5-15 上午7:48 
Description: 
"""

from socket import *

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 9001
    BUFFSIZE = 1024
    ADDR = (HOST,PORT)

    tcpClientSocket = socket(AF_INET,SOCK_STREAM)
    tcpClientSocket.connect(ADDR)

    while True:
        data = input('> ').strip()

        if not data:
            break

        tcpClientSocket.send(data.encode())

        data = tcpClientSocket.recv(BUFFSIZE).decode()

        if not data:
            break

        print(data)

    tcpClientSocket.close()
    