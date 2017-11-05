#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: lgonline 
@license: Apache Licence  
@contact: lgonline@hotmail.com 
@site:  
@software: PyCharm 
@file: Tcp_Socket_Client.py 
@time: 10/22/17 10:44 PM 
"""

from socket import *

def func():
    HOST = '::1'
    PORT = 8001
    BUFSIZE = 1024
    ADDR = (HOST,PORT)

    tcp_Clienet_Sock = socket(AF_INET,SOCK_STREAM)
    tcp_Clienet_Sock.connect(ADDR)

    while True:
        data = raw_input('>')
        if not data:
            break
        tcp_Clienet_Sock.send(data)
        data = tcp_Clienet_Sock.recv(BUFSIZE)
        if not data:
            break
    tcp_Clienet_Sock.close()

    pass


class main():
    def __init__(self):
        func()
        pass


if __name__ == "__main__":
    main()
    pass  