# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 12:49
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : example_35_1.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com


"""
如下两个函数都存在一些问题，主要在于
数据的表示完全暴露，对象使用和操作实现对具体的表现强依赖
需要把对象的使用与具体的实现进行隔离
"""

#这样写程序会遇到非常麻烦的管理问题
# def fun(a1,a2,b1,b2):
#     num = a1*b2 + a2*b1
#     den = a2 * b2
#     print num
#     print den
#     pass
#
# #更新后的版本，但未考虑特殊的有理数，不能将它与其它元组相互区分
# r1 = (3, 5)
# r2 = (7, 15)
# def adv_dev(r1,r2):
#     num = r1[0]*r2[1] + r2[0]*r1[1]
#     den = r1[1]*r2[1]
#     print num
#     print den

class recommended_fun():
    def __init__(self,num,den=1):
        self.num = num
        self.den = den

    def plus(self,another):
        den = self.den * another.den
        num = ((self.num*another.den) + (self.den*another.num))
        return recommended_fun(num,den)

    def myprint(self):
        print str(self.num)+"/"+str(self.den)


if __name__ == '__main__':
    # print '-------excute fun--------'
    # print fun(3,5,7,15)
    # print '-------excute adv_fun--------'
    # print adv_dev(r1,r2)
    print '-------excute recommended_fun--------'
    r1 = recommended_fun(3,5)
    r2 = r1.plus(recommended_fun(7,15))
    r2.myprint()