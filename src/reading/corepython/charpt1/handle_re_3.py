#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: 330mlcc 
@license: Apache Licence  
@contact: lg_online@126.com 
@site:  
@software: PyCharm 
@file: handle_re_3
@time: 18-5-9 下午10:56 
Description: 
"""
import re

if __name__ == '__main__':
    print(re.findall('car','Mcar, the car is very beautiful!'))

    str = 'this and that'
    print(re.findall(r'(th\w+) and (th\w+)',str,re.I))

    print('---------字符串替换---------')
    print(re.sub('[ae]','X','abcdefg'))
    print(re.subn('[ae]', 'X', 'abcdefg'))

    print('---------字符串分割---------')
    data = {'Mountain view, CA94040',
            'Sunnyvale,CA',
            'Los Altos,94023',
            'Cupertino 95014',
            'Palo Alto CA'}

    for datum in data:
        print(re.split(', |(?= (?:\d{5}|[A-Z]{2}))',datum))
        # print('------------------')
        # print(re.split(',', datum))
        # # print(re.split(', |(?= (?:\d{5}|[A-Z]{2})'),datum)

    print('----------------------------')

    for datum in data:
        # print(re.split(', |(?= (?:\d{5}|[A-Z]{2}))',datum))
        # print('------------------')
        print(re.split(',', datum))
        # print(re.split(', |(?= (?:\d{5}|[A-Z]{2})'),datum)

    print('----------------------------')

    for datum in data:
        print(re.split(', |(?= ([A-Z]{2}))',datum))
    
    