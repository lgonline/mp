#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/9 9:50
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : p8_1-2.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com
# @Description: 
#   
#   

from math import hypot

class Vector:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r %r)' % (self.x,self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)



def main():
    vector1 = Vector(2,4)
    vector2 = Vector(3,6)
    print(vector1+vector2)
    print(abs(vector1))
    print(vector2.__mul__(3))
    pass


if __name__ == '__main__':
    main()
    pass