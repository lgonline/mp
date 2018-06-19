#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/14 12:34
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : link_web_crawler.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com

import requests
import re
from urllib.parse import urljoin

link_re = re.compile(r'href="(.*?)"')

def main(url):
    req = requests.get(url)
    # print('init req is : ',req)

    # print(req.status_code)
    if(req.status_code != 200):
        return []

    # print(req.text)

    links = link_re.findall(req.text)

    print("\nFound {} links".format(len(links)))

    for link in links:
        link = urljoin(url,link)
        print(link)

    pass


if __name__ == '__main__':
    main('http://www.sina.com.cn')
