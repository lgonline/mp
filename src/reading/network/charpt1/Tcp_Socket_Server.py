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
import time

def main():
    HOST = ''
    PORT = 8001
    BUFSIZE = 1024
    ADDR = (HOST,PORT)

    tcpServerSock = socket(AF_INET,SOCK_STREAM)
    tcpServerSock.bind(ADDR)
    tcpServerSock.listen(1)

    while True:
        print('waiting for connection...')
        tcpCliSock,addr = tcpServerSock.accept()
        print('...connected from : ',addr)
        while True:
            data = tcpCliSock.recv(BUFSIZE)
            data = data.decode('utf-8')
            if not data:
                break
            ss = '[%s] %s' % (time.ctime(),data)
            tcpCliSock.sendall(ss.encode('utf-8'))
            print(ss)
        tcpCliSock.close()
    tcpServerSock.close()

    pass

#
# class main():
#     def __init__(self):
#         func()
#         pass


if __name__ == "__main__":
    main()
    pass  