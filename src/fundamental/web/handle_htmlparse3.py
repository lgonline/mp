#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

from urllib.request import urlopen


if __name__ == "__main__":
    content = urlopen('http://www.4hb.com/letters/ltrdelacct4.html').read()
    pass