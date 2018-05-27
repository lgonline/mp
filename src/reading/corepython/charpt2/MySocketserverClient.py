#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: 330mlcc 
@license: Apache Licence  
@contact: lg_online@126.com 
@site:  
@software: PyCharm 
@file: MySocketserverClient
@time: 18-5-15 上午9:11 
Description: 
"""
import socket

if __name__ == '__main__':
    client = socket.socket()    ##定义协议类型,相当于生命socket类型,同时生成socket连接对象
    client.connect(('127.0.0.1',9002))

    while True:
        msg = input('> ').strip()

        if len(msg) == 0 :continue

        client.send(msg.encode())

        data = client.recv(1024)
        print('recv:> ',data.decode())

    client.close()
    pass 
    
    