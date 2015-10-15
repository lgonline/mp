__author__ = 'Administrator'

import socket,time

socket.setdefaulttimeout(3)

def socket_port(ip,port):
    try:
        if port >= 65535:
            print('port scan is over')
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result = s.connect_ex((ip,port))
    except:
        pass
    pass