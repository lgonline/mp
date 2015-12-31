#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

a = lambda x,y : x*y

'''
递归实现
'''

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


'''
函数的属性
'''
def wrap(func):
    '''
    call(*args,**kwargs):
        return func(*args,**kwargs)

    call.__doc__ = func.__doc__
    call.__name__ = func.__name__
    call.__dict__.update(func.__dict__)
    return call
    '''

def hello():
    print("hello world")

if __name__ == "__main__":
    print(a(2,7))
    print(factorial(5))
    wrap(hello())