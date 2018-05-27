#!/usr/bin/python
__author__ = 'ethan'

import os
import pwd

if __name__ == "__main__" :
    print('os.getlogin() is : ',os.getuid())
    print('pwd.getpwuid is : ',pwd.getpwuid(os.getuid()))
    #print(os.getlogin())

    for id in pwd.getpwall():
        print(id)