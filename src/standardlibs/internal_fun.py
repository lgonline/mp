#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

sorts = [1,2,3,4,5,6]
str = 12345

def useAll():
    print(all(sorts))

def useAny():
    print(any(sorts))

def useBin():
    #mybinnumbers = bin(str)
    print(bin(str))
    #print(bin(str1))

def useCmp():
    print()

def useType():
    print(type(sorts))

if __name__ == "__main__":
    useAll()
    useAny()
    useBin()
    useCmp()
    useType()