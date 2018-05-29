#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: 330mlcc 
@license: Apache Licence  
@contact: lg_online@126.com 
@site:  
@software: PyCharm 
@file: handle_re_1
@time: 18-5-5 下午4:30 
Description: 
"""
import re

if __name__ == '__main__':
    #使用match方法匹配字符串
    m = re.match('foo','food on the table')
    print(m.group())

    #使用search方法在字符串种查找
    s1 = re.search('foo','feed on the table')
    if s1 is not None:
        print(s1.group())
    else:
        print('s1.search is none.')

    #匹配多个字符串
    bt = 'bat|bet|bit'
    s2 = re.search(bt,'this is a bat on the bit')
    if s2 is not None:
        print(s2.group())

    #匹配任何单个字符
    print('****************匹配任何单个字符****************')
    anyend = '.end'
    s31 = re.match(anyend,'bend')
    s32 = re.match(anyend, 'end')
    s33 = re.match(anyend, '\nend')
    print('.end匹配bend')
    if s31 is not None:
        print(s31.group())
    else:
        print('can not match')
    print('.end匹配end')
    if s32 is not None:
        print(s31.group())
    else:
        print('can not match')
    print('.end匹配\nend')
    if s33 is not None:
        print(s31.group())
    else:
        print('can not match')

    print('****************字符集匹配****************')
    strm1 = re.match('[cr][23][dp][o2]','c3po')
    print("m = re.match(\'[cr][23][dp][o2]\',\'c3po\') is ",strm1.group())
    strm2 = re.match('[cr][23][dp][o2]', 'c2do')
    print("m = re.match(\'[cr][23][dp][o2]\',\'c2do\') is ", strm2.group())
    strm3 = re.match('r2d2|c3po', 'c2do')
    if strm3 is not None:
        print("m = re.match(\'r2d2|c3po\',\'c3po\') is ",strm3.group())
    else:
        print('can not match')
    strm4 = re.match('r2d2|c3po', 'r2d2')
    if strm4 is not None:
        print("m = re.match(\'[cr][23][dp][o2]\',\'c2do\') is ", strm4.group())
    else:
        print('can not match')

    print('****************重复和特殊分组****************')
    #(\w+\.)？表示主机名是可选的，见括号中的内容
    patt1 = '\w+@(\w+\.)?\w+\.com'
    print(re.match(patt1,'liugang9@jd.com').group())
    print(re.match(patt1, 'liugang9@www.jd.com').group())
    patt2 = '(\w\w\w)-(\d\d\d)'
    print(re.match(patt2,'abc-123').group(1))
    print(re.match(patt2,'abc-123').group(2))
    print(re.match(patt2, 'abc-123').group())