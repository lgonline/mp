#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = '330mlcc'

#推倒式
numbers = list(range(1,5))
print numbers

numbers_list = [numbers2 for numbers2 in range(1,6)]
numbers_list.append(numbers2)
print 'number_list is : ', numbers_list

number_list2 = [number3 for number3 in range(1,6) if number3 % 2 == 0]
print 'number_list2 is : ',number_list2

'''
rows = range(1,4)
cols = range(1,3)
for row in rows:
    for col in cols:
        print(rows,cols)
'''
#以上代码等同于
rows = range(1,4)
cols = range(1,3)

cells = [(rows,cols) for row in rows for col in cols]
for row , col in cells:
    print row,col


if __name__ == '__main__':
    pass

