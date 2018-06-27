#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/26 20:25
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : p26_namedtuple.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com

from collections import namedtuple
city = namedtuple('city','name country population coordinates')
tokto = city('tokyo','JP',36.933,(35.689722,139.691667))

def main():
    print(tokto)
    print(tokto.population)
    print(tokto.coordinates)
    pass


if __name__ == '__main__':
    main()
