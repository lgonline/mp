#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = '330mlcc'

import socket

host = '127.0.0.1'
port = 9001
bufsize = 1024
addr = (host,port)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(addr)

while True:
    data = input('>')

    if not data:
        continue

        print('input data:[%s]' % data)

    s.send(data.encode('utf-8'))

    rdata = s.recv(bufsize)

    if not data:
        break

# print(s.recv(1024))
#
# for data in ['michael','tracy','sarah']:
#     s.send(data.encode())
#     # print(s.recv(1024))
#
# s.send(b'exit')

if __name__ == '__main__':
    pass

