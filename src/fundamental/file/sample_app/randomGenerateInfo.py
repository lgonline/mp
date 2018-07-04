#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/4 20:27
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : randomGenerateInfo.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com
# @Description: 
#   
#   

from urllib.request import urlopen
import re,os
from bs4 import BeautifulSoup

def main():
    target_page = urlopen('https://zhidao.baidu.com/question/202829791.html')
    # print(type(target_page))
    # print(target_page.info())
    contents = target_page.read()
    bs = BeautifulSoup(contents,'html.parser')
    print(bs.prettify())
    # contents = re.findall('',str(target_page.read())de)
    # print(str(contents).encode('utf-8'))
    #print(contents.decode('utf-8'))

    # contents = re.findall(r'',target_page.read())
    pass


if __name__ == '__main__':
    main()
    pass