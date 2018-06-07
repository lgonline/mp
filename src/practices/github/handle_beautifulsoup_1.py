#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 19:10
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : handle_beautifulsoup_1.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com

"""

"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def useUrllibGetWebpage():
    html = urlopen('https://www.baidu.com')
    print(html.read())
    pass

def useBeautifulSoupGetWebpage():
    url = 'https://www.baidu.com'
    webpage = urlopen(url)
    soup = BeautifulSoup(webpage,'html.parser')
    print(soup)

def getBookFromDouban():
    url = 'https://www.douban.com/tag/%E5%B0%8F%E8%AF%B4/?focus=book'
    soup = BeautifulSoup(urlopen(url),'html.parser')
    # book_div = soup.find(attrs={'id':'book'})
    books = soup.findAll(attrs={'class':'title'})
    # print(type(books))
    # for book in books:
    #     print(book)

    for book in books:
        clear_books = re.findall(r'>(\S+)<',str(book))
        print(clear_books)

    # for mybook in clear_books:
        # print(mybook)

if __name__ == '__main__':
    # useUrllibGetWebpage()
    # useUrllibGetWebpage()
    getBookFromDouban()