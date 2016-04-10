#!/usr/bin/python
__author__ = 'Administrator'

import os
import pwd

getlogin = os.getlogin()
getuid = os.getuid()
getpwuid = pwd.getpwuid(os.getuid())

print("os.getlogin() is : ", getlogin)
print("os.getudi() is : ", getuid)
print("pwd.getpwuid(os.getuid()) is : ",getpwuid)

for id in pwd.getpwall():
    print(id[0])