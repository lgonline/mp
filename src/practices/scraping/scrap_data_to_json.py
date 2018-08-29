#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 14:33
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : scrap_data_to_json.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com
# @Description: 
#   
#   

import requests
import urllib.request
from bs4 import BeautifulSoup

def main():
    urls = 'https://www.zhihu.com/search?q=scrapy&type=content'
    UserAgent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    Referer = 'https://www.zhihu.com'
    headers = {'UserAgent':UserAgent,'Referer':Referer,'Connection':'keep-alive','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}
    cookies = '''
    _xsrf=54GoD98eUO7BiJThnLpT7sHkDfj9LwF2; d_c0="ABDnoGHI1g2PTmFkc0GUyAsRdgxUZHRksck=|1530532125"; q_c1=e09e0c536533440fba1ecf1358fd66d0|1530532125000|1530532125000; _zap=670e3f9e-d94c-41a0-8312-216b16e14f88; l_cap_id="NWQ4MGUyYTQ0NTczNGVhMzkxZGU5ZWRlM2QyMDY0YmQ=|1530534988|dca7820714db6f3d8f107e58b4f38914e1dc7660"; r_cap_id="MTg1NzQ4Yzc1OTVkNGQxYzlhZWI4ZjE3NzQ4ZGJlZWE=|1530534988|f7eeb95805cdb35af14f5defbe82b126a72c7aea"; cap_id="NzBjYTI3NGRmOTQzNDMwNWIyNWYwZjM4N2QxNWViMWU=|1530534988|a392e844e9c4ff59e0e38afa7d1e5d5df66b1202"; capsion_ticket="2|1:0|10:1530535011|14:capsion_ticket|44:MzFiMGNkYzgwNTY3NDA2NGJkYjEzOWU5MTEwM2RhNWY=|437a592e60913cc80243ffa17179d3862edd0c993f03c1ad8dc9eb79c59c2d53"; z_c0="2|1:0|10:1530535041|4:z_c0|92:Mi4xb3FxbkJRQUFBQUFBRU9lZ1ljaldEU2NBQUFDRUFsVk5nYWxoV3dERWlUbXNLSHBzOFZOUXVwcHAtaFJLTVMtR2xB|9b5b25faf93168db1fe1766193765aea57c9155a358105455e6943b6c405972a"; tgw_l7_route=9553ebf607071b8b9dd310a140c349c5
    '''
    # req = urllib.request.get(urls,headers=headers,cookie=cookies)
    # responses = urllib.request.urlopen(req)
    # soup = BeautifulSoup(responses,'lxml',from_encoding='gbk')
    # print(soup)

    wbdata = requests.get(urls,headers=headers,cookies=cookies)
    soup = BeautifulSoup(wbdata, 'lxml', from_encoding='gbk')
    print(soup)

if __name__ == '__main__':
    main()
    pass