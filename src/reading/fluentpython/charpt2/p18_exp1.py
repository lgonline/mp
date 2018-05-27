#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = '330mlcc'


"""
演示列表推导式
"""
symbols = 'abcd'
codes = []

if __name__ == '__main__':
    # 把一个字符串变成unicode码,最常见的写法
    # for symbol in symbols:
    #     codes.append(ord(symbol))
    #     print(codes)

    # 把一个字符串变成unicode码,python风格的写法
    # code = [ord(symbol) for symbol in symbols]
    # print(code)

    # 条件表达式
    # beyond_ascii = [ord(symbol) for symbol in symbols]
    # beyond_ascii = [ord(symbol) for symbol in symbols if ord(symbol) > 99]
    # print(beyond_ascii)

    '''用生成器表达式初始化元祖和数组'''
    symbols = '刘沛成'
    for i in range(10):
        for j in range(10):
            print(symbols)
    # print(tuple(ord(symbol) for symbol in symbols))
    pass

