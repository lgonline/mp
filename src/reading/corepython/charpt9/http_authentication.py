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
@file: http_authentication.py
@time: 18-6-6 下午10:10 
Description: 
"""
import urllib.request,urllib.error,urllib.parse

LOGIN = 'wesley'
PASSWD = "you'll never guess"
URL = "http://localhost"
REALM = 'Secure Achive'

def handler_versiion(url):
    hdlr = urllib.request.HTTPBasicAuthHandler()    #http验证类 里面有用户名和密码
    # print('init : ',hdlr)
    # print(type(hdlr))
    hdlr.add_password(REALM, urllib.parse.urlparse(url)[1],LOGIN,PASSWD)    #将url 用户名 密码添加进去
    # print('after : ',hdlr)
    opener = urllib.request.build_opener(hdlr)  #urlopen不支持验证等高级功能 所以自定义opener
    # print('opener : ',opener)
    urllib.request.install_opener(opener)   #建立url开启器
    # print('urllib.request.install_opener(opener) is : ',urllib.request.install_opener(opener))
    # print('url is : ',url)
    return url

def request_version(url):
    from base64 import b64encode
    req = urllib.request.Request(url)  #开始请求页面
    b64str = b64encode(bytes('%s:%s' % LOGIN,PASSWD),'utf-8')#将sting转换成base64-data形式 base64为一种形式的二进制编码
    req.add_header("Authorization","Basic %s" % b64str) #添加header标头
    return req

for funcType in ('handler', 'request'):
    print('***Using %s:' % funcType.upper())
    url = eval('%s_version' % funcType)(URL)    #eval 将字符串转换成有效的表达式并返回结果
    f = urllib.urlopen(url)
    print(f.readline())
    f.close()
#
# if __name__ == '__main__':
#     handler_versiion('http://www.baidu.com')
#     main()
#     pass
#
    