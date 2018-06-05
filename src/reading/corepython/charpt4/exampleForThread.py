#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: 330mlcc 
@license: Apache Licence  
@contact: lg_online@126.com 
@site:  
@software: PyCharm 
@file: exampleForThread
@time: 18-5-20 下午8:59 
Description: 可对比出单线程和多线程的区别
-------------Demo for single thread---------------
starting at :  Tue May 29 23:09:26 2018
start a single thread 1 at :  Tue May 29 23:09:26 2018
the single thread 1 is done at :  Tue May 29 23:09:30 2018

start a single thread 2 at :  Tue May 29 23:09:30 2018
the single thread 2 is done at :  Tue May 29 23:09:32 2018

-------------Demo for muti thread---------------
start a muti-thread 1 at :  Tue May 29 23:09:32 2018
start a muti-thread 2 at :  Tue May 29 23:09:32 2018
the muti-thread 2 is done at :  Tue May 29 23:09:34 2018

the muti-thread 1 is done at :  Tue May 29 23:09:36 2018

all of the thread was done at :  Tue May 29 23:09:38 2018
"""

import _thread
from time import ctime,sleep

def singleThread1():
    print('start a single thread 1 at : ',ctime())
    sleep(4)
    print('the single thread 1 is done at : ',ctime(),'\n')

def singleThread2():
    print('start a single thread 2 at : ',ctime())
    sleep(2)
    print('the single thread 2 is done at : ',ctime(),'\n')

def muti_Thread1():
    print('start a muti-thread 1 at : ',ctime())
    sleep(4)
    print('the muti-thread 1 is done at : ',ctime(),'\n')

def muti_Thread2():
    print('start a muti-thread 2 at : ',ctime())
    sleep(2)
    print('the muti-thread 2 is done at : ',ctime(),'\n')

loops = [4,2]
def loop(nloop,nsec,lock):
    print('start loop : ',nloop,'at : ',ctime())
    sleep(nsec)
    print('loop : ', nloop, 'done at : ', ctime())
    lock.release()      # 当sleep时间到的时候，释放锁


def main():
    print('-------------Demo for single thread---------------')
    print('starting at : ',ctime())
    # 增加的使用线程进行处理
    singleThread1()
    singleThread2()
    # thread.start_new_thread(mutibThread,())
    # sleep(6)
    # singleThread()
    # mutibThread()
    print('-------------Demo for muti thread---------------')
    _thread.start_new_thread(muti_Thread1, ())
    _thread.start_new_thread(muti_Thread2, ())
    sleep(6)
    print('all of the thread was done at : ',ctime())

    print('-------------The thread lock demo for muti thread---------------')
    print('starting thread lock demo at',ctime())
    locks = []                      # 创建一个锁的列表
    nloops = range(len(loops))      #

    for i in nloops:
        lock = _thread.allocate_lock()      # 使用thread.allocate_lock()函数得到锁对象
        lock.acquire()                      # 通过acquire方法获得每个锁，效果相当于把锁所伤
        locks.append(lock)

    for i in nloops:
        _thread.start_new_thread(loop,(i,loops[i],locks[i]))

    for i in nloops:
        while locks[i].locked():
            pass
    print('all of the thread was done at : ', ctime())




if __name__ == '__main__':
    main()
    
    