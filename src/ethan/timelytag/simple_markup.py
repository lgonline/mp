#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

'''
    创建一个简单的标记脚本，打印一些开始标记、每个用段落标签括起来的块；打印结束标记
'''

import sys,re
from make_util import *

print("<html><head><title>...</title><body>")

title = True

for block in blocks(sys.stdin):
    block = re.sub(r'\*(.+?)\*',r'<em>\l</em>',block)
    if title:
        print('<h1>')
        print(block)
        print('</h1>')
        title = False
    else:
        print('<p>')
        print(block)
        print('</p')

print("</body></html>")