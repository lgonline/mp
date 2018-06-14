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
    def num(self):
        return self.__num

    def den(self):
        return self.__den

    #定义了一个局部使用的求最大公约数的静态方法
    @staticmethod
    def gcd(m,n):
        if n == 0:
            m, n = n, m

        while m != 0:
            m, n = n % m, m

        return n

    def __init__(self,num,den):
        #在开始出检查参数的类型和分母的值
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError

        if den == 0:
            raise ZeroDivisionError

        # sign = 1
        #
        # if num < 0:
        #     num,sign = -num, -sign
        #
        # if den < 0:
        #     den, sign = -den, -sign
        #
        # g = recommended_fun.gcd(num,den)

        # self.__num = sign * (num//g)
        # self.__den = den // g
        self.__num = num
        self.__den = den
        # print self.__num
        # print self.__den

    def __add__(self,another):
        # print '-----init-------'
        # print 'self.__den : ',self.__den
        # print 'self.__num : ', self.__num
        # print 'another.__den : ', another.__den
        # print 'another.__num : ', another.__num
        den = self.__den * another.den()
        # print '-----after-------'
        # print 'self.__den : ', self.__den
        # print 'self.__num : ', self.__num
        # print 'another.__den : ', another.__den
        # print 'another.__num : ', another.__num
        # print 'den : ',den

        num = (self.__num * another.den() + self.__den * another.num())
        # print '-----after ii-------'
        # print 'self.__den : ', self.__den
        # print 'self.__num : ', self.__num
        # print 'another.__den : ', another.__den
        # print 'another.__num : ', another.__num
        # print 'num : ',num
        # print '2 : ',self.__num
        return recommended_fun(num,den)

    def __mul__(self, another):
        return recommended_fun(self.__num * another.num(),self.__den * another.den())

    def __floordiv__(self, another):
        if another.num() == 0:
            raise  ZeroDivisionError

        return recommended_fun(self.__num * another.den(),self.__den * another.num())

    def __eq__(self,another):
        return self.__num * another.den() == self.__den * another.num()

    def __lt__(self, another):
        return self.__num * another.den() < self.__den * another.num()

    def __str__(self):
        print(str(self.__num)+"/"+str(self.__den))

    def myprint(self):
        print(self.__num,"/",self.__den)


if __name__ == '__main__':
    # print '-------excute fun--------'
    # print fun(3,5,7,15)
    # print '-------excute adv_fun--------'
    # print adv_dev(r1,r2)
    # print '-------excute recommended_fun--------'
    # r1 = recommended_fun(3,5)
    # r2 = r1.__add__(recommended_fun(7,15))
    # # r2.printself()
    # r2.myprint()
    x = recommended_fun(3,5)
    x.myprint()

    y = x.__add__(recommended_fun(7,15))

    y.myprint()
