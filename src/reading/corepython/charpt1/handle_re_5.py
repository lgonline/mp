#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: 330mlcc 
@license: Apache Licence  
@contact: lg_online@126.com 
@site:  
@software: PyCharm 
@file: handle_re_5
@time: 18-5-14 下午11:30 
Description: 
"""

import re

if __name__ == '__main__':
    f = open('messages.txt','r')
    for eachline in f:
        print(re.findall(r'(\S{3} \d{2} \d{2}:\d{2}:\d{2}) (\S{3}) (\S+)\[(\d{4})\]:(.* \S .*)',eachline))
    f.close()
    pass 
    
    