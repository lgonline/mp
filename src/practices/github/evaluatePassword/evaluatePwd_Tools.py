#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/8 15:09
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : evaluatePwd_Tools.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com

"""

"""

def saveFile(dict_name):
    f = open('temp.txt','w')
    f.write(str(dict_name))
    f.close()

def readFile():
    f = open('temp.txt','r')
    a = f.read()
    # print(a)
    return eval(a)

if __name__ == '__main__':
    # readFile()
    pass