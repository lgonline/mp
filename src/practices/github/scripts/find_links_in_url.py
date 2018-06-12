#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/12 20:37
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : find_links_in_url.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com

"""

"""

import requests,re

def main():
    url = input('please enter a url:\n')
    websit = requests.get(url)
    html_content = websit.text

    links = re.findall('href="//(.*)/"',html_content) or re.findall('src="//(.*)/"')
    print(type(links))
    print(len(links))

    for link in links:
        print(link)

    pass


if __name__ == '__main__':
    main()
