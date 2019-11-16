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
@file: useDict.py
@time: 18-6-7 下午11:24 
Description: 
"""


def handleDict():
    mydict = {'day': 'Aperiod of twenty-four hours that never misses',
              'positive': 'Mistaken at the top of one\'s voice',
              'misfortune': 'The kind of fortune that never misses'}
    print(mydict)
    lol = [['a', 'b'], ['c', 'd'], ['e', 'fo']]
    print('使用dict转换为字典：', dict(lol))
    # print(mydict1)
    pass

def addCompInDict():
    mydict = {'a':1,'b':2}
    print(mydict)
    # 使用[key]添加或修改元素
    mydict['c'] = 3
    print(mydict)

    mydict['m'] = 'a'
    print(mydict)

def main():
    # handleDict()
    addCompInDict()



if __name__ == '__main__':
    main()
    pass 
    
    