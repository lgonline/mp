#!/usr/bin/env python  
# -*- coding: utf-8 -*-

""" 
@version: v1.0 
@author: 330mlcc 
@Software: PyCharm
@license: Apache Licence  
@Email   : mlcc330@hotmail.com
@contact: 3323202070@qq.com
@site:  
@software: PyCharm 
@file: handleInit.py
@time: 18-6-13 下午7:14 
Description: __init__方法用于对类的初始化，两个例子，使用init更可懂
"""

class Rectangle:
    def area(self):
        return self.length * self.width


class advanceRectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


#在子类种实现__init__()方法

if __name__ == '__main__':
    r = Rectangle()
    r.length,r.width = 5,8
    print('r.length,r.width = 5,8 is : ',r.area())

    ar = advanceRectangle(5,15)
    print('r.length,r.width = 5,15 is : ', ar.area())
    pass 
    
    