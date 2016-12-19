#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = 'liugang9'

import re

def re_txt():
    line = "pic.jcloud.com						404"
    matchObj = re.match(r'(.*)\t+(.*)',line,re.M|re.I)
    for i in (1,2):
        print matchObj.group(i)

if __name__ == '__main__':
    re_txt()
