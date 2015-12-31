#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

'''
简单输出斐波那契數列前 N 个数
'''
'''
deffab(max):
   n, a, b =0, 0, 1
   whilen < max:
       printb
       a, b =b, a +b
       n =n +1
'''

'''
要提高 fab 函数的可复用性，最好不要直接打印出数列，而是返回一个list
第二版
'''
'''
def fab(max):
    n,a,b = 0,0,1
    list = []
    while n < max:
        list.append(b)
        #print(b)
        a, b = b,a+b
        n = n + 1
    return list
'''

'''
该函数在运行中占用的内存会随着参数 max 的增大而增大，如果要控制内存占用，最好不要用 List来保存中间结果，而是通过iterable对象来迭代
Fab 类通过 next() 不断返回数列的下一个数，内存占用始终为常数
第三版
'''
class Fab(object):
    def __init__(self,max):
        self.max = max
        self.n,self.a,self.b = 0,0,1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            r = self.b
            self.a,self.b = self.b,self.a+self.b
            self.n = self.n + 1
            return r
        raise StopIteration()

'''
class 改写的这个版本，代码远远没有第一版的fab函数来得简洁。如果要保持第一版的简洁性，同时又要获得iterable的效果
'''
def fab(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n=n+1

if __name__ == "__main__":
    #print(fab(5))
    for n in Fab(5):
        print(n)

    for x in fab(5):
        print(x)
