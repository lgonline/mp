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
@file: handleCookieCrawler.py
@time: 18-6-23 上午12:46 
Description: 
"""

import urllib.request
import http.cookiejar
import os

url = 'http://news.163.com/photoview/00AN0001/2294452.html'

def main():


    # 以字典的形式设置header
    headers = {'Host': 'news.163.com','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Language': 'en-US,en;q=0.5','Accept-Encoding': 'gzip, deflate',
               'Referer': 'news.163.com/'}

    # 设置cookie
    cjar_cookies = http.cookiejar.CookieJar()
    # proxies = urllib.request.ProxyHandler({'http':'127.0.0.1：8080'})
    proxies = urllib.request.ProxyHandler({})

    # opener通常是build_opener()创建的opener对象。
    opener = urllib.request.build_opener(proxies,urllib.request.HTTPSHandler,urllib.request.HTTPCookieProcessor(cjar_cookies))
    # print('opener通常是build_opener()创建的opener对象。')
    # print(opener,'\n')

    # 建立空列表，为了指定格式的headers信息
    headall = []

    # 通过for循环遍历字典，构造指定格式的headers信息
    # print('通过for循环遍历字典，构造指定格式的headers信息\n')
    for key,value in headers.items():
        item = (key,value)
        # print(item)
        headall.append(item)

    # 将指定格式的headers信息添加好
    opener.addheaders = headall
    # print('\n-----------将指定格式的headers信息添加好------------------')
    # print(opener.addheaders)

    # 将opener安装为全局
    # install_opener(opener) 安装opener作为urlopen()使用的全局URL opener，即意味着以后调用urlopen()时都会使用安装的opener对象。
    urllib.request.install_opener(opener)
    html_data = urllib.request.urlopen(url).read().decode('utf-8')
    # data = html_data.read().decode('utf-8')
    fhandle = open(os.path.abspath('handleCookieCraoler.html'),'wb')
    fhandle.write(html_data)
    fhandle.close()

    pass


if __name__ == '__main__':
    main()
    pass 
    
    