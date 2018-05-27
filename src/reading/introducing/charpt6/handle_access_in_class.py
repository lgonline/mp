#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: lgonline 
@license: Apache Licence  
@contact: lgonline@hotmail.com 
@site:  
@software: PyCharm 
@file: handle_access_in_class.py 
@time: 11/3/17 11:48 PM 
"""

"""
"""


class Duck():
    def __init__(self,input_name):
        self.hidden_name = input_name
        print self.hidden_name

    def get_name(self):
        print 'inside the getter.'
        return self.hidden_name
        print self.hidden_name

    def set_name(self,input_name):
        print 'inside the setter.'
        self.hidden_name = input_name
        print input_name

    name = property(get_name,set_name)


#使用修饰符定义属性的方法
class Duck2():
    def __init__(self,input_name):
        self.hidden_name = input_name

    @property
    def name(self):
        print 'inside the getter.'
        return self.hidden_name

    @name.setter
    def name(self,inputname):
        print 'inside the getter.'
        self.hidden_name = inputname

def func():
    pass


class main():
    fowl = Duck('Howard_q')
    #fowl.name

    #
    fowl.set_name('Diff')
    fowl.name

    fowl2 = Duck2('aaa')
    print fowl2.name
    print '*************************'
    fowl2.name = 'abc'
    print fowl2.name
    def __init__(self):
        pass


if __name__ == "__main__":
    main()
    pass  