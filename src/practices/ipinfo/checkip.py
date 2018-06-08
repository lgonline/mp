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

def ISIP(s):
    return len([i for i in s.split('.') if (0<=int(i)<=255)]) == 4

def searchFromIP(ip):
    uip = urllib.urlopen('http://m.ip138.com/ip.asp?ip=%s' % ip)
    fip = uip.read().decode('utf-8')
    # print(fip)
    #<h1 class="query">您查询的IP：8.8.8.8</h1><p class="result">本站主数据：美国 Google免费DNS</p><p class="result">参考数据一：美国</p><p class="result">网友提交的IP：美国 Google
    try:
        if fip != "":
            rip = re.compile(r"您查询的IP：(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).*本站主数据：(\S+\s{1,3}\S+)<.*参考数据一：(\S+)<.*网友提交的IP：(\S+\s{1,3}\S+).*")
            # rip = re.compile(r"您查询的IP：(.*)")
            # rip = re.compile(r"本站主数据：(\S+\s{1,4}\S+)</p>.*参考数据一：(\S+\s{1,4}\S+)</p>.*网友提交的IP：(\S+ \S+)</p>.*")
            results = rip.findall(fip)
            print(results)
        else:
            rip = re.compile(r"您查询的IP：(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).*本站主数据：(\S+\s{1,4}\S+)</p>.*参考数据一：(\S+\s{1,4}\S+)</p>.*")
            # rip = re.compile(r"本站主数据：(\S+\s{1,4}\S+)</p>.*参考数据一：(\S+\s{1,4}\S+)</p>.*")
            results = rip.findall(fip)
    except Exception as e:
        print(e)

    print('%s\t %s' % (ip,results))
    # for result in results:
    #     for r in result:
    #         print(r.decode('utf8'))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('please enter a ip address')
        sys.exit()
    input = sys.argv[1]
    # if not re.findall()
    if ISIP(input):
        ipadress = input
        searchFromIP(ipadress)
        print('done')
    else:
        print('ip is not found.')
