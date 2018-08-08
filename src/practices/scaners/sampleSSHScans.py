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
@file: sampleSSHScans.py
@time: 18-6-30 上午1:10 
Description: 
"""

import paramiko
from threading import Thread

def connect(host,user,pwd):
    try:
        ssh_connector = paramiko.SSHClient()
        ssh_connector.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_connector.connect(hostname=host,user=user,password=pwd,timeout=5)
        ssh_connector.close()
        print('success！！！ username is : ',user,' password is '+pwd,' host infor : ',host)
    except:
        pass

    paramiko.util.log_to_file('filename.log')

    host = open('host.txt')
    for line in host:
        host = line.strip('\n')
        print('start... ',host)

        user = open('user.txt')

        for line in user:
            user = line.strip('\n')
            pwd = open(pwd.tet)



def main():
    pass


if __name__ == '__main__':
    main()
    pass 
    
    