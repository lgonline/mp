#!/usr/bin/env python  
# -*- coding: utf-8 -*-

""" 
@version: v1.0 
@author: 330mlcc 
@Software: PyCharm
@license: Apache Licence  
@Email   : mlcc330@hotmail.com
@contact: 3323202070@qq.com
@site:  
@software: PyCharm 
@file: handleAsyncoreDispatcher.py
@time: 18-7-1 下午4:25 
Description: 
"""


import time,socket,asyncore,threading

'''
服务器端数据响应类，接收数据并把数据原样发回。
'''
class EchoHandler(asyncore.dispatcher_with_send):
    def handle_read(self):
        data = self.recv(1024)
        if data:
            self.send(data)


'''
响应服务器端程序，负责监听一个端口，并响应客户端发送的消息然后原样返回给客户端。
其中handle_accept()方法定义当一个连接到来的时候要执行的操作，这里指定了使用一个Handler来出来发送来的数据。
'''
class EchoServer(asyncore.dispatcher):
    def __init__(self,host,port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host,port))
        self.listen(5)

    def handle_accept(self):
        conn,addr = self.accept()
        print('Incomint connection from %s' % repr(addr))

'''
响应服务客户端程序，负责连接响应服务器
'''
class EchoClient(asyncore.dispatcher):
    def __init__(self,host,port):
        asyncore.dispatcher.__init__(self)
        # messages 定义了一个要发送的消息列表，每次发送一个消息，知道列表为空为止。
        self.messages = ['1','2','3','4','5','6','7','8','9','10']
        self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connect((host,port))

    def handle_connect(self):
        pass

    def handle_close(self):
        self.close()

    def handle_read(self):      # 处理接收到的数据，这里把收到的数据打印的终端上。
        print(self.recv(1024))

    def writable(self):         # 判断是否有数据可以向服务器端发送。
        return (len(self.messages) > 0)

    def handle_write(self):     # 当writable()函数返回True时，写入数据。
        if len(self.messages) > 0:
            self.send(self.messages.pop(0))

'''
用来启动服务器端程序的线程。
'''
class EchoServerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        server = EchoServer('localhost',9999)
        asyncore.loop()

'''
用来启动客户端端程序的线程。
'''
class EchoClientThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        client = EchoClient('localhost',9999)
        asyncore.loop()


if __name__ == '__main__':
    # main()

    EchoServerThread().start()
    time.sleep(2)
    EchoClientThread().start()
    pass 
    
    