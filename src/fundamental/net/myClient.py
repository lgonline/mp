__author__ = 'Administrator'

import socket,sys
from urllib.request import urlparse

def httpServer(url):
    u = urlparse(url)
    host = u[1]
    page = u[2]
    s = socket.socket()
    port =80
    s.connect((host,port))
    httpcmd = 'get'+page+'\n'
    s.send(httpcmd)
    s.close()

if __name__ == '__main':
    httpServer()