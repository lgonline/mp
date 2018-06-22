#!/usr/bin/env python  
# -*- coding: utf-8 -*-

""" 
@version: v1.0 
@author: 330mlcc 
@Software: PyCharm
@license: Apache Licence  
@Email   : mlcc330@hotmail.com
@contact: 3323202070@qq.com
@site:  
@software: PyCharm 
@file: handleGetCrawler.py
@time: 18-6-22 下午11:30 
Description: 
"""

import urllib.request
import os

keyword = 'cctv5'
url = 'https://www.so.com/s?ie=utf-8&fr=none&src=360sou_newhome&q='+keyword
# print(url)
def main():
    try:
        requests = urllib.request.Request(url)
        data = urllib.request.urlopen(requests).read()
        content = open(os.path.abspath('aaa.html'),'wb')
        content.write(data)
        content.close()
        print(data)
    except urllib.request.HTTPError as httperrors:
        print(httperrors.code)
        print(httperrors.reason)
    except urllib.request.URLError as urlerrors:
        print(urlerrors.reason)
    pass


if __name__ == '__main__':
    main()
    pass 
    
    