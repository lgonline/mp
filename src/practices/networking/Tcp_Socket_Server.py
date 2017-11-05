#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: lgonline 
@license: Apache Licence  
@contact: lgonline@hotmail.com 
@site:  
@software: PyCharm 
@file: Tcp_Socket_Server.py
@time: 10/22/17 10:35 PM 
"""

from socket import *
from time import ctime

def func():
    HOST = ''
    PORT = '8001'
    BUFSIZE = 1024
    ADDR = (HOST,PORT)

    tcpServerSock = socket(AF_INET,SOCK_STREAM)
    tcpServerSock.bind(ADDR)
    tcpServerSock.listen(5)

    while True:
        print 'waiting for connection...'
        tcpCliSock,addr = tcpServerSock.accept()
        print '...connected from : ',addr
        while True:
            data = tcpServerSock.recv(BUFSIZE)
            if not data:
                break
            tcpCliSock.send('[%s] %s'(ctime(),data))
        tcpCliSock.close()
    tcpServerSock.close()

    pass


class main():
    def __init__(self):
        func()
        pass


if __name__ == "__main__":
    main()
    pass  