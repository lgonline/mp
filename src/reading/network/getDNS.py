#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = 'liugang5'

'''
实现DNS查询
'''

import sys,socket

def searchDNS(hosts):
    hosts = sys.argv[1]
    result = socket.getaddrinfo(hosts,None,0,socket.SOCK_STREAM)
    #print(result[0][4])

    counter = 0

    for item in result:
        print(counter,item[4])
        counter += 1

if __name__ == "__main__":
    searchDNS()
    pass