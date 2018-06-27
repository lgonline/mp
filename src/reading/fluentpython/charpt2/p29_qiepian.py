#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/26 20:39
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : p29_qiepian.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com
# @Description: list,tuple,str的切片操作
#   
#   


def main():
    l = [10,20,30,40,50,60]
    print(l[:2])
    print(l[::-1])
    print(l[:-3])
    print(l[-5:-3])

    str ='abcdef'
    print(str[:2])
    print(str[::-1])
    print(str[:-3])
    print(str[-5:-3])
    pass


if __name__ == '__main__':
    main()
    pass