#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: 330mlcc 
@license: Apache Licence  
@contact: lg_online@126.com 
@site:  
@software: PyCharm 
@file: handle_re_4
@time: 18-5-10 上午1:12 
Description: 
"""

import os
import re

if __name__ == '__main__':
    f = os.popen('who','r')
    for eachline in f:
        print(re.split(r'\s\s+}\t',eachline.rstrip()))
    f.close()

    print('----------re中的扩展符号------------')

    print(re.findall(r'(?i)yes','yes? Yes YES!!!'))
    print(re.findall(r'(?im)(^th[\w ]+)',"""this line is the first,another line, that line, it\'s the best"""))
    print(re.findall(r'th.+', """The first line
     the second line 
     the chird line"""))#The是大写
    print('-------findall(r\'th.+\'和r\'(?s)th.+\'以及r\'(?im)th.+\'的区别---------------')
    print(re.findall(r'(?s)th.+',"""The first line
     the second line 
     the chird line"""))
    print('-------findall(r\'th.+\'和r\'(?s)th.+\'以及r\'(?im)th.+\'的区别---------------')
    print(re.findall(r'(?im)th.+', """The first line
         the second line 
         the chird line"""))

    print('---------------更加易读的正则表达式-------------')
    print(re.search(r'''(?x)
                    \((\d{3})\)
                    [ ]     #匹配空格
                    (\d{3})
                    -       #匹配横线
                    (\d{4})
                    ''','(800) 555-1212').groups())

    print('---------对正则表达式进行分组----------')
    print(re.findall(r'http://(?:\w+\.)*(\w+\.com)','http://www.baidu.com http://sina.com http://google.com'))
    print(re.search(r'http://(?:\w+\.)*(\w+\.com)', 'http://www.baidu.com http://sina.com http://google.com').groups())
    print(re.search(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})','(800) 555-1212').groupdict())
    print(re.search(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?P<number>\d{4}) (?P=areacode)-(?P=prefix)-(?P=number)','(800) 555-1212 800-555-1212').groupdict())
    print(re.match(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?P<number>\d{4}) (?P=areacode)-(?P=prefix)-(?P=number) (?P=areacode)(?P=prefix)(?P=number)',
                  '(800) 555-1212 800-555-1212 8005551212'))

    print('---------清晰的表达多个正则表达式--------------')
    # print(bool(re.match(r'\((?P<areacode>)\d{3})\) (?P<prefix>\d{3})-(?P<number>\d{4}) (?P=areacode)-(?P=prefix)-(?P=number) (?P=areacode)(?P=prefix)(?P=number)',
    #                     '(800) 555-1212 800-555-1212 8005551212')))
    pass 
    
    