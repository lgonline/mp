#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = '330mlcc'

import os,socket,threading

from ..charpt1 import Tcp_Socket_Server

SERVER_HOST = 'localhost'
SERVER_PORT = 0
BUF_SIZE = 1024
ECHO_MSG = 'Hello, echo Server.'

class ForkingClient():
    '''A client to test forking server.'''
    def __init__(self,ip,port):
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.connect((ip,port))

    def run(self):
        current_process_id = os.getpid()
        print('PID %s Sending echo message to the sersver : ')

if __name__ == '__main__':
    pass

