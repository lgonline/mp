#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = '330mlcc'

if __name__ == '__main__':
    pass


import socket

#创建套接字，必须使用socket.socket()函数

#TCP连接,socket.AF_INET表示基于网络的套接字,socket.SOCK_STREAM表示面向连接的TCP套接字
tcpsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#UDP连接,socket.AF_INET表示基于网络的套接字,socket.SOCK_DGRAM表示面向连接的TCP套接字
psocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
