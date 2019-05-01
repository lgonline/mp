#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
@author: mlcc
@file: Point.py
@time: 19-5-1 下午5:32 
Description: 
"""

import math

class Point:
    def __init__(self):
        self.reset()

    def pointMove(self,x,y):
        self.x = x
        self.y = y
        return x,y

    def pointAddMove(self,x,y):
        pass

    def reset(self):
        self.move(0,0)

    # 计算移动的位置到原点的距离
    def calcZeorDistance(self,x,y):
        distance = math.sqrt((x)**2 + (y)**2)
        return distance

if __name__ == '__main__':
    p1 = Point()
    p1.pointMove(3,4)
    # print(p1.x)
    p1_distance = p1.calcZeorDistance(p1.x,p1.y)
    print(p1_distance)

    p1.pointMove(40,30)
    p1_distance2 = p1.calcZeorDistance(p1.x,p1.y)
    print(p1_distance2)
    pass