#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: 330mlcc 
@license: Apache Licence  
@contact: lg_online@126.com 
@site:  
@software: PyCharm 
@file: MyFTP
@time: 18-5-16 上午1:07 
Description: 
"""

from ftplib import FTP

import ftplib
import os
import socket

HOST = 'ftp.mozilla.org'
DIRN = 'pub/mozilla.org/webtools'
FILE = 'bugzilla-latest.tar.gz'

def main():
    try:
        f = ftplib.FTP(HOST)
    except (socket.error,socket.gaierror) as e:
        print('EROR: cannot reach "%s' % HOST)
        return
    print('*** Connected to host %s' % HOST)

    try:
        f.login()
    except ftplib.error_perm:
        print('ERROR: cannot login anonymously')
        f.quit()
        return
    print('*** Logged in as "anonymous"')

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print('ERROR: cannot CD to "%s"' % DIRN)
        f.quit()
        return
    print('*** Changed in as "anonymous"')

    try:
        f.retrbinary('RETR %s',(l))
    except ftplib.error_perm:
        print('ERROR: cannot CD to "%s"' % DIRN)
        f.quit()
        return
    print('*** Changed in as "anonymous"')

if __name__ == '__main__':
    ftps = FTP('192.168..31')
    ftps.login('anonymous','abc@sina.com')
    ftps.dir()
    #ftps.quit()

    pass 
    
    