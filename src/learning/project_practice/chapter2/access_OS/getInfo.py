#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

import os

current_login_user = ''
current_login_uid = ''

def getUserInfo():
    #get login information form os
    current_login_user = os.getlogin()
    current_login_uid = os.getuid()
    print("current_login_user is ",current_login_user," and current_login_uid is ",current_login_uid)

if __name__ == "__main__":
    getUserInfo()
    #print(os.getlogin())