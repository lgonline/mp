#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

'''
    urlparse:URL字符串的拆分
    urlunparse:URL字符串的拼接
'''

from urllib.parse import urlparse
from urllib.parse import urlunparse
from urllib.parse import urljoin
from urllib.parse import quote
from urllib.parse import quote_plus
from urllib.parse import unquote
from urllib.parse import unquote_plus

if __name__ == "__main__":
    print('----------------------using urlparse----------------------------')
    inputurl = urlparse('http://m.blog.csdn.net:9090/blog/xing_anksh/17240975/login.do?uid=01923&passd=93875')
    print(inputurl)
    print(inputurl.scheme)
    print(inputurl.hostname)
    print(inputurl.port)

    print('----------------------using urlunparse----------------------------')

    myurl = urlunparse(('http', 'm.blog.csdn.net', '/blog/xing_anksh/17240975/login.do','', 'uid=01923', ''))
    print(myurl)

    print('----------------------using urljoin----------------------------')
    myurl2 = urljoin('http://m.blog.csdn.net:9090/blog/','xing_anksh/17240975/login.do')
    print(myurl2)

    print('----------------------URL decode or encode----------------------------')

    #cowork = urlparse('http://cowork.cn.lenovo.com/promotions/town%20hall%20meeting/ciotopprojects/_layouts/15/AccessDenied.aspx?Source=http%3A%2F%2Fcowork%2Ecn%2Elenovo%2Ecom%2Fpromotions%2Ftown%20hall%20meeting%2Fciotopprojects%2FLists%2FGoNoGo%2FNewForm%2Easpx%3FSource%3Dhttp%3A%2F%2Fcowork%2Ecn%2Elenovo%2Ecom%2Fpromotions%2Ftown%252520hall%252520meeting%2Fciotopprojects%2FLists%2FGoNoGo%2Foverview%2Easpx&Type=list&name=f4d83851%2Da89f%2D4996%2Dacce%2D11e1c77a243f')
    myurl3 = 'http://m.blog.csdn.net:9090/blog/xing_anksh/17240975/login.do?uid=01923&passd=93875'
    handle_quote = quote(myurl3)
    handle_quote_plus = quote_plus(myurl3)
    handle_unquote = unquote(handle_quote)
    handle_unquote_plus = unquote_plus(handle_quote_plus)
    print('befor decode or encode : ',myurl3)
    print('after quote : ',handle_quote)
    print('after quote_plus : ',handle_quote_plus)
    print('after unquote : ',handle_unquote)
    print('after unquote_plus : ',handle_unquote_plus)
    #print('after quote',myurl3.quote)