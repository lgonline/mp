#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: 330mlcc 
@license: Apache Licence  
@contact: lg_online@126.com 
@site:  
@software: PyCharm 
@file: hrm
@time: 18-5-21 下午11:09 
Description: 
"""

import datetime

class PersonValueError(TypeError):
    pass

class PersonTypeError(TypeError):
    pass

class Person:
    _num = 0

    @classmethod
    def num(cls):
        return Person._num

    def __init__(self,name,sex,birthday,ident):
        if not (isinstance(name, str) and sex in ('女','男')):
            raise PersonValueError(name,sex)

        try:
            birth = datetime.date(*birthday)
        except:
            raise PersonValueError('Wrong date:',birthday)

        self._name = name
        self._sex = sex
        self._birthday = birth
        self._id = ident

        Person._num += 1

    def id(self):
        return self._id

    def name(self):
        return self._name

    def sex(self):
        return self.sex

    def birthday(self):
        return self.birthday

    def age(self):
        return (datetime.date.today().year - self._birthday.year)

    def __set_name__(self, name):
        if not isinstance(name,str):
            raise PersonValueError('set_name',name)
        self._name = name

    def __lt__(self,another):
        if not isinstance(another,Person):
            raise PersonTypeError(another)
        return self._id < another._id

    def __str__(self):
        return "".join(self._id,self._name,self._sex,str(self._birthday))

    def details(self):
        print(", ".join(('编号 ： '+self._id,' 姓名 ： '+self._name,'性别 ： '+self._sex,'出生日期 ： '+str(self._birthday))))




if __name__ == '__main__':
    p1 = Person('liugang9','女',(1995,7,30),'1201510111')
    p1.details()
    pass 
    
    