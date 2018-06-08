#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/4 12:09
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : checkip.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com

import urllib
import re
import sys
from bs4 import BeautifulSoup

def ISIP(s):
    return len([i for i in s.split('.') if (0<=int(i)<=255)]) == 4

def searchFromIP(ip):
    uip = urllib.urlopen('http://m.ip138.com/ip.asp?ip=%s' % ip)
    fip = uip.read().decode('utf-8')
    soup = BeautifulSoup(fip, 'html.parser')
    key_points = soup.find(attrs={'class': 'module'})
    results = key_points.findAll(attrs={'class': 'result'})
    for result in results:
        details = re.findall(r'>\S+：(.*)<',str(result))
        detail = str(details[0]).decode('utf-8')
        print(detail)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('please enter a ip address')
        sys.exit()
    input = sys.argv[1]
    # if not re.findall()
    if ISIP(input):
        ipadress = input
        searchFromIP(ipadress)
        # print('done')
    else:
        print('ip is not found.')
