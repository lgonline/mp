#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

from urllib import request
#from string import *
from string import ascii_letters, digits, hexdigits

if __name__ == "__main__":
    responses = request.urlopen("http://www.lenovo.com.cn")
    print(responses.read().decode("gbk"))