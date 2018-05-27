#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = '330mlcc'

'''
基于笛卡尔积，做一些tshirt的列表
'''

colors = ['black','white']
sizes = ['s','m','l']

if __name__ == '__main__':
    t_shirts = [(tshirt,size) for tshirt in colors for size in sizes ]
    print(t_shirts)
    pass

