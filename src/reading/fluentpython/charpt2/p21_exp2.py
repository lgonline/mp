#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = '330mlcc'

'''
基于笛卡尔积，做一些tshirt的列表
'''

colors = ['black','white']
sizes = ['s','m','l']

if __name__ == '__main__':
    print('--------------比较一下两个不同的列表生成器导致的不同-----------------')
    t_shirts1 = [(color,size) for color in colors for size in sizes ]
    print("t_shirts1 = [(color,size) for color in colors for size in sizes ] is : ",t_shirts1)

    t_shirts2 = [(color, size) for size in sizes for color in colors ]
    print("t_shirts2 = [(color, size) for size in sizes for color in colors ] is : ",t_shirts2)

    print('--------------比较一下生成器导致的不同-----------------')
    for t_shirts3 in ('%s %s' % (c, s) for c in colors for s in sizes):
        print(t_shirts3)
    pass

