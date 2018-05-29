#!/usr/bin/python
#-*- coding: utf-8 -*-
#第四章简述的是判断和迭代
__author__ = '330mlcc'

def using_zip():
    days = ['Monday','Tuesday','Wednesday']
    fruits = ['banana','orange','peach']
    drinks = ['coffee','tea','beer']
    dsserts = ['tiramisu','ice cream','pie','pudding']
    for days, fruits,drinks,deserts in zip(days,fruits,drinks,dsserts):
        print(days,": drink", drinks,'- eat',fruits,'- enjoy',deserts )

#推导式，使用循环快速生成数据结构
def tuidao():
    #创建整数列表
    lists = list(number for number in range(1,10))
    lists1 = list(number-1 for number in range(1, 10))
    print lists
    print lists1
    #创建一个偶数列表
    oushu_list = list(number for number in range(1,20) if number % 2 == 0)
    print oushu_list
    #循环的多层嵌套的推导
    rows = range(1,4)
    cols = range(1,3)
    while_list = [(row,col) for row in rows for col in cols]
    for whilelist in while_list:
        print whilelist

if __name__ == '__main__':
    #using_zip()
    tuidao()

