#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

import urllib.request

if __name__ == "__main__":
    '''
        basicly method to use urllib
    '''
    response = urllib.request.urlopen("http://www.python.org")
    mybyte = response.read()
    mystr = mybyte.decode("urf8")

    response.close()

    print(mystr)