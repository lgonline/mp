__author__ = 'Administrator'

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port  = 1234
s.connect(host,port)
#call the function of recv to get the data come from server side
print(s.recv(1024))
s.close()