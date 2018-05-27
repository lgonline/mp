#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: 330mlcc 
@license: Apache Licence  
@contact: lg_online@126.com 
@site:  
@software: PyCharm 
@file: MyTimestampServer
@time: 18-5-15 上午12:44 
Description: 
"""

from socket import *
from time import ctime

if __name__ == '__main__':
    HOST = ''
    PORT = 9001
    BUFFSIZE = 1024
    ADDR = (HOST, PORT)

    tcpServerSocket = socket(AF_INET,SOCK_STREAM)   #创建服务器套接字
    tcpServerSocket.bind(ADDR)                      #套接字与地址绑定
    tcpServerSocket.listen(5)                       #监听连接，传入连接请求的最大数

    while True:
        print('waiting for connection...')
        tcpClientScoket,addr = tcpServerSocket.accept()
        print('... connected from : ',addr)

        while True:
            data = tcpClientScoket.recv(BUFFSIZE).decode()
            print('data=',data)

            if not data:
                break

            # tcpClientScoket.send('[%s] %s' % (ctime(),data))  #python2的写法
            tcpClientScoket.send(('[%s] %s' % (ctime(), data)).encode())

        tcpClientScoket.close()
    tcpServerSocket.close()
    pass 
    
    