#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/21 15:52
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : handleRequests.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com

"""

"""

import requests

# 设置代理
proxies = {
    "http":"127.0.0.1:8080",
    "http":"http://user:pass@127.0.0.1:8080/"
}

url = "http://www.baidu.com"

def main():
    html_content = requests.get(url)
    # 使用代理，是否允许url跳转等参数
    # html_content = requests.get(url,proxies=proxies,verrify=False，allow_redirects=False)

    print(html_content)
    pass


if __name__ == '__main__':
    main()
