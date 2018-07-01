#!/usr/bin/python
#-*- coding: utf-8 -*-

# __author__ = '330mlcc'
#
# import socket
# import time
# import threading
#
# def tcplink(sock,addr):
#     print('accetp new connection for %s:5S...' % addr)
#     sock.send('welcome!'.encode())
#     while True:
#         data = socket.recv(1024)
#         time.sleep(5)
#
#         if data == 'exit' or not data:
#             break
#
#         sock.send('hello : '.encode()+data)
#
#     socket.close()
#     print('Connection from %s:%s' % addr)
#
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#
# s.bind(('127.0.0.1',9001))
#
# s.listen(5)
#
# print('waiting for connection....')
#
# while True:
#     sock,addr = s.accept()
#     t = threading.Thread(target=tcplink(),args=(socket,addr))
#     t.start()

import socket
import time

host = ''    #host设定为空，表示可以与任何ip的socket在端口9001通信
port = 9001
bufsize = 1024

quit = False
shutdown = False

addr = (host,port)

##设置socket,AF_INET表示是IPV4标准，SOCK_STREAM是TCP传输协议
tcpConnServers = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpConnServers.bind(addr)
tcpConnServers.listen(1)

while True: #与客户端建立连接之后，获取客户端传来的数据
    print('watting for connection...')
    tcpConnClients,ddr = tcpConnServers.accept()  # 不断监听获取新的客户端连接
    print('connected from : ', addr)

    while True:
        data = tcpConnClients.recv(bufsize)
        data = data.decode('utf-8')

        if not data:
            break

        ss = '[%s] %s' % (time.time(),data)
        print(ss)

    if data == 'bye':
        quit = True
        break
    elif data == 'shutdown':
        shutdown = True
        break
        print('server has been closed')

if __name__ == '__main__':
    pass

