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
Description: 
"""

import thread
from time import ctime,sleep

def singleThread():
    print('start a single thread at : ',ctime())
    sleep(4)
    print('the single thread is done at : ',ctime(),'\n')

def mutibThread():
    print('start a mutib thread at : ',ctime())
    sleep(2)
    print('the mutib thread is done at : ',ctime(),'\n')

def main():
    print('starting at : ',ctime())
    # 增加的使用线程进行处理
    thread.start_new_thread(singleThread,())
    thread.start_new_thread(mutibThread,())
    sleep(6)
    # singleThread()
    # mutibThread()
    print('all of the thread was done at : ',ctime())

loops = [4,2]
def loop(nloop,nsec,lock):
    print('start loop : ',nloop,'at : ',ctime())
    sleep(nsec)
    print('loop : ', nloop, 'done at : ', ctime())
    lock.release()

if __name__ == '__main__':
    main()
    
    