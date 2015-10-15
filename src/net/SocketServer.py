__author__ = 'Administrator'

import socket

#the example for socket server
'''
socketserver = socket.socketpair(socket.AF_INET,socket.SOCK_STREAM)
hostname = socket.gethostname()
port = 1234
socketserver.bind((hostname,port))
socketserver.listen(5)

while True:
    c,addr = socketserver.accept()
    print("The connection come from ",addr)
    c.send("congratulations! a sample server was created")
    c.close()
'''

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('localhost',8001))
sock.listen(5)
while True:
    connection,address = sock.accept()
    try:
        connection.settimeout(5)
        buf = connection.recv(1024)
        if buf == '1':
            connection.send('Welcome to server!')
        else:
            connection.send('Please go out!')
    except socket.timeout as e:
        print(e)
    connection.close()