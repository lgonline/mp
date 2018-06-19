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
@file: getUrlFromSina.py
@time: 18-6-19 下午8:25 
Description: 
"""

import urllib.request
import re

# def getUrl(input_content):
#     content = re.findall(r'href="//(.*)/"',input_content)
#     return content

def getInfoSimple():
    # myinput = input('please enter a url your wanted.\n')
    myinput = 'https://blog.csdn.net/weixin_42061676/article/details/80713875'
    html_content = urllib.request.urlopen(myinput)
    content = html_content.read()
    print(content)

def getHtmlInfoUsingHeader():
    myinput = 'https://blog.csdn.net/weixin_42061676/article/details/80713875'
    headers = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36")
    #使用build_opener()修改报头
    openers = urllib.request.build_opener()
    openers.add_handler = [headers]
    data = openers.open(myinput).read()

    #使用add_header()添加报头
    req = urllib.request.Request(myinput)
    req.add_header("User-Agent","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36")
    data2 = urllib.request.urlopen(req).read()
    print(data2)

def getHtmlInfoUsingTimeout():
    myurl = 'https://blog.csdn.net/weixin_42061676/article/details/80713875'
    # myurl = 'https://www.google.com'

    # headers = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36")
    for i in range(1,100):
        try:
            file = urllib.request.urlopen(myurl,timeout=1)
            data = file.read()
            print(len(data))
        except Exception as e:
            print('error infor : %s' % e)

def getHtmlInfoUsingProxy(proxy_addr,url):
    httphd = urllib.request.HTTPHandler(debuglevel=1)
    httpshd = urllib.request.HTTPSHandler(debuglevel=1)
    proxy = urllib.request.ProxyHandler({'http':proxy_addr})
    # opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler,httphd,httpshd)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode('utf-8')
    return data

def main():
    urlfilecontent = urllib.request.urlopen('http://www.sina.com.cn')
    # print(type(urlfilecontent))
    files = urlfilecontent.read()
    # print(getUrl(files))
    print(files)
    # print(type(files))
    # for file in files:
    #     print(file)
    # with open(urlfilecontent) as files:
    #
    #     print(files)
    pass


if __name__ == '__main__':
    # main()
    # getInfoSimple()
    # getHtmlInfoUsingHeader()
    # getHtmlInfoUsingTimeout()
    proxy_addr = '202.75.210.45:7777'
    data = getHtmlInfoUsingProxy(proxy_addr,"https://www.iqiyi.com")
    print(len(data))
    pass 
    
    