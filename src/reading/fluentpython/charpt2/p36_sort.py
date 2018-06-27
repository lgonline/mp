#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/26 20:56
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : p36_sort.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com
# @Description: 
#   
#   


def main():
    fruits = ['grape','raspberry','apple','banana']
    print(sorted(fruits))               # 新建一个按照字母排序的字符串列表
    print(sorted(fruits,reverse=True))  # 按照字母降序排列
    print(sorted(fruits,key=len))       # 按照长度降序排列
    pass



if __name__ == '__main__':
    main()
    pass