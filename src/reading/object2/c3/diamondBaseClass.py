#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
@author: mlcc
@file: diamondBaseClass.py
@time: 19-5-3 上午9:49 
Description: 钻石继承问题,这是一个基类
"""

class DiamondBase:
    num_base_calls = 0

    def callme(self):
        print("Calling mehtod on Base Class.")
        self.num_base_calls += 1
        print("num_base_calls is : ", self.num_base_calls)

class LeftSubClass(DiamondBase):
    num_left_calls = 0

    def callme(self):
        # DiamondBase.callme(self)
        super().callme(self)
        print("Calling method on Left Subclass.")
        self.num_left_calls += 1
        print("num_base_calls is : ", self.num_left_calls)


class RightSubClass(DiamondBase):
    num_right_calls = 0

    def callme(self):
        # DiamondBase.callme(self)
        super().callme()
        print("Calling method on Right Subclass.")
        self.num_right_calls += 1
        print("num_base_calls is : ", self.num_right_calls)

class DiamondSubClass(LeftSubClass,RightSubClass):
    num_sub_calls = 0

    def callme(self):
        # LeftSubClass.callme(self)
        # RightSubClass.callme(self)
        super().callme()
        print("Calling method on Subclass.")
        self.num_sub_calls += 1
        print("num_base_calls is : ", self.num_sub_calls)

if __name__ == '__main__':
    s = DiamondSubClass()
    s.callme()
    print("s.num_base_calls is : ",s.num_base_calls)
    print("s.num_left_calls is : ", s.num_left_calls)
    print("s.num_right_calls is : ", s.num_right_calls)
    print("s.num_sub_calls is : ", s.num_sub_calls)
    pass