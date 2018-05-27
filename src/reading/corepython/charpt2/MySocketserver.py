#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: 330mlcc 
@license: Apache Licence  
@contact: lg_online@126.com 
@site:  
@software: PyCharm 
@file: MySocketserver
@time: 18-5-15 上午9:02 
Description:
socket并不能多并发，只能支持一个用户，socketserver 简化了编写网络服务程序的任务，socketserver是socket的在封装。
socketserver在python2中为SocketServer,在python3种取消了首字母大写，改名为socketserver。

socketserver中包含了两种类，一种为服务类（server class），一种为请求处理类（request handle class）。
前者提供了许多方法：像绑定，监听，运行…… （也就是建立连接的过程） 后者则专注于如何处理用户所发送的数据（也就是事务逻辑）。

socketserver一共有这么几种类型：
1. class socketserver.TCPServer(server_address, RequestHandlerClass, bind_and_activate=True)
2. class socketserver.UDPServer(server_address, RequestHandlerClass, bind_and_activate=True)
3. class socketserver.UnixStreamServer(server_address, RequestHandlerClass, bind_and_activate=True)
4. class socketserver.UnixDatagramServer(server_address, RequestHandlerClass,bind_and_activate=True)
"""

import socketserver

class MyTCPHandle(socketserver.BaseRequestHandler): #服务类，监听绑定等等
    def handle(self):                               #请求处理类，所有请求的交互都是在handle里执行的
        self.data = self.request.recv(1024).strip() #每一个请求都会实例化MyTCPHandler(socketserver.BaseRequestHandler)
        print('{} wrote : '.format(self.client_address[0])) #sendall是重复调用send.
        print(self.data)

        self.request.sendall(self.data.upper())

if __name__ == '__main__':
    HOST,PORT = 'localhost',9002

    server = socketserver.TCPServer((HOST,PORT),MyTCPHandle)

    server.serve_forever()

server = socketserver.ThreadingTCPServer((HOST,PORT),MyTCPHandle)       #线程
# server  = socketserver.ForkingTCPServer((HOST, PORT), MyTCPHandler)   #多进程 linux适用
# server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    
    