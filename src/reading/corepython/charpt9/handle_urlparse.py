#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: 330mlcc 
@license: Apache Licence  
@contact: lg_online@126.com 
@site:  
@software: PyCharm 
@file: handle_urlparse
@time: 18-6-6 下午8:59 
Description: 
"""

from urllib.parse import urlparse
from urllib.request import urlopen

def main():
    test_url = 'http://blog.sina.com.cn/s/blog_16694e3f90102ygzi.html'
    lists = (urlparse(test_url))
    # print(list[i] for i in range(len(lists) for list in lists))
    print(lists)
    # print(lists.)

    f = urlopen(test_url)
    # print(f.read().decode('utf-8'))
    print(f.info())
    print(f.fileno())

if __name__ == '__main__':
    main()
    pass 
    
    