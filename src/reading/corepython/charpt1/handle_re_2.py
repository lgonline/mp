#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: 330mlcc 
@license: Apache Licence  
@contact: lg_online@126.com 
@site:  
@software: PyCharm 
@file: handle_re_2
@time: 18-5-5 下午5:34 
Description: 
"""

import re

if __name__ == '__main__':
    print('*************匹配字符串的起始和结尾以及单词边界*****************')
    #patt1 =
    print(re.match('^The','The big apple').group())
    # print(re.match(r'\bThe', 'end. The big apple').group())
    # print(re.match(r'\bThe', 'biteThe big apple').group())
    # print(re.match(r'\BThe', 'biteThe big apple').group())
    pass