#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: lgonline 
@license: Apache Licence  
@contact: lgonline@hotmail.com 
@site:  
@software: PyCharm 
@file: handle_itertools.py 
@time: 11/3/17 11:20 PM 
"""

"""
itertools包含特殊用途的迭代器函数，在for...in循环中调用迭代函数，每次返回一项并记住当前调用的状态
"""

import itertools

def func():

    for items in itertools.chain([1,2],['a','b']):
        print items

    #cycle是一个在它的参数之间循环的无限迭代器
    #for item in itertools.cycle([1,2]):
    #    print item
    #import itertools
    #accumulate计算累计的值
    for item2 in itertools.count(1,2):
        print item2

class main():
    func()
    def __init__(self):
        pass


if __name__ == "__main__":
    main()
    pass  