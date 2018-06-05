#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = '330mlcc'

import threading
from time import sleep,ctime

'''创建thread的实例，传递给它一个函数'''
loops = [4,2]
def loop(nloop,nsec):
    print('start loop ',nloop,' at : ',ctime())
    sleep(nsec)
    print('loop ',nloop, ' done at : ',ctime())

'''创建thread的实例，传递给它一个可调用的类实例'''
loops1 = [4,2]
class threadFun(object):
    def __init__(self,func,args,name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)

def loop1(nloop,nsec):
    print('start loop ',nloop,' at : ',ctime())
    sleep(nsec)
    print('loop1 ',nloop, ' done at : ',ctime())

def main():
    print('starting at : ',ctime())
    threads = []
    nloops = range(len(loops))
    # print('len(loops)',len(loops))

    # 创建thread的实例，传递给它一个函数
    # for i in nloops:
    #     t = threading.Thread(target=loop,args=(i,loops[i]))
    #     threads.append(t)

    # 创建thread的实例，传递给它一个可调用的类实例
    for i in nloops:
        t = threading.Thread(target=threadFun(loop1,(i,loops[i]),loop1.__name__))
        threads.append(t)


    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('All done at : ',ctime())

if __name__ == '__main__':
    main()
    pass

