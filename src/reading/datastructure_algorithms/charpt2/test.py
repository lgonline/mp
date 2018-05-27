# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 21:07
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : test.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com

"""

"""


if __name__ == '__main__':
    class recommended_fun():
        def num(self):
            return self.__num

        def den(self):
            return self.__den

        # 定义了一个局部使用的求最大公约数的静态方法
        @staticmethod
        def gcd(m, n):
            if n == 0:
                m, n = n, m

            while m != 0:
                m, n = n % m, m

            return n

        def __init__(self, num, den):
            self.__num = num
            self.__den = den

        def __add__(self, another):
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
            print('den : ', den)

            num = (self.__num * another.den() + self.__den * another.num())
            # print '-----after ii-------'
            # print 'self.__den : ', self.__den
            # print 'self.__num : ', self.__num
            # print 'another.__den : ', another.__den
            # print 'another.__num : ', another.__num
            print('num : ', num)

            return recommended_fun(num, den)

        def myprint(self):
            print(self.__num, "/", self.__den)


    if __name__ == '__main__':
        x = recommended_fun(3, 5)
        print(x.myprint())
        y = x.__add__(recommended_fun(7, 15))
        y.myprint()
