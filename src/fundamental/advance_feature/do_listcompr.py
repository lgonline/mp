#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = 'liugang5'

if __name__ == "__main__":
    L1 = ['Hello', 'World', 18, 'Apple', None]
    L2 = [s.lower() for s in L1 if isinstance(s,str) is True]
    print(L2)