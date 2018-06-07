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
    # print(fip)
    soup = BeautifulSoup(fip,'html.parser')
    key_points = soup.find(attrs={'class':'module'})
    print(str(key_points.strings).decode('utf-8'))
    results = key_points.find(attrs={'class': 'result'})
    #print(type(results))
    print(str(results).decode('utf-8'))
    #for key_point in key_points:
    for result in results:
    #    myresult = re.findall(r'>(.*)<', result)
        print(result)
    # try:
    #     if fip != "":
    #         rip = re.compile(r"您查询的IP：(\d+.\d+.\d+.\d+).*本站主数据：(\S+)</p>.*参考数据一：(\S+\s{1,4}\S+)</p>.*网友提交的IP：(\S+ \S+)</p>")
    #         # rip = re.compile(r"本站主数据：(\S+\s{1,4}\S+)</p>.*参考数据一：(\S+\s{1,4}\S+)</p>.*网友提交的IP：(\S+ \S+)</p>.*")
    #         results = rip.findall(fip)
    #     else:
    #         rip = re.compile(r"您查询的IP：(\d+.\d+.\d+.\d+).*本站主数据：(\S+\s{1,4}\S+)</p>.*参考数据一：(\S+\s{1,4}\S+)</p>.*")
    #         # rip = re.compile(r"本站主数据：(\S+\s{1,4}\S+)</p>.*参考数据一：(\S+\s{1,4}\S+)</p>.*")
    #         results = rip.findall(fip)
    # except Exception as e:
    #     print(e)
    #
    # # print('%s\t %s' % (ip,str(results).decode('utf8')))
    # for result in results:
    #     for r in result:
    #         print(r.decode('utf8'))

if __name__ == '__main__':
    # if len(sys.argv) < 2:
    #     print('please enter a ip address')
    #     sys.exit()
    # input = sys.argv[1]
    # # if not re.findall()
    input = "8.8.8.8"
    if ISIP(input):
        ipadress = input
        searchFromIP(ipadress)
    else:
        print('ip is not found.')
