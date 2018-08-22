#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
@version: v1.0 
@author: 330mlcc 
@Software: PyCharm
@license: Apache Licence  
@Email   : mlcc330@hotmail.com
@contact: 3323202070@qq.com
@site:  
@software: PyCharm 
@file: mutiProcessUsingFork.py
@time: 18-6-19 下午11:18 
Description: 
"""

import os
import threading
from multiprocessing import Process
from time import ctime,sleep
from multiprocessing import Pool
import os, time, random

def createProcessUsingFork():
    print('current process %s start ....' % (os.getpid()))
    pid = os.fork()
    if pid < 0:
        print('error in fork.')
    elif pid == 0:
        print('I am child process %s and my parent process is %s' % (os.getpid(),os.getppid()))
    else:
        print('I %s created a child process %s ' % (os.getpid(),pid))
    pass

def run_proc(name):
    print('child process %s %s running...' % (name,os.getpid()))

# def createProcessUsingMultiprocessing():
#     print('Parent process %s.' % os.getpid())
#     for i in range(10):
#         p = Process(target=run_proc(),args=(str(i),))
#         print('Process will start.')
#         p.start()
#     p.join()
#     print('Process end.')


def music(name):
    for i in range(3):
        print('I was listening to %s. %s' % (name,ctime()))
        sleep(1)

def move(name):
    for i in range(3):
        print('I was at the %s! %s' % (name,ctime()))
        sleep(3)

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__ == '__main__':
    createProcessUsingFork()
    # createProcessUsingMultiprocessing()

    # 不使用多线程
    # music('aaa')
    # move('bbb')
    # print("all over %s" % ctime())

    # 使用多线程
    threads = []
    t1 = threading.Thread(target=music, args=(u'aaa'))
    threads.append(t1)
    t2 = threading.Thread(target=music, args=(u'bbb'))
    threads.append(t2)

    for t in threads:
        t.setDaemon(True)
        t.start()

    print("all over %s" % ctime())



    print('--------------------')
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(20):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    # when the object of pool call the method of join(), then it will waiting until all of the sub-threads is end
    p.join()
    print('All subprocesses done.')


    print('--------线程锁错误的写法---------')
    # 假定这是你的银行存款:
    balance = 0


    def change_it(n):
        # 先存后取，结果应该为0:
        global balance
        balance = balance + n
        balance = balance - n


    def run_thread(n):
        for i in range(100000):
            change_it(n)


    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)

    print('--------线程锁正确的写法---------')
    # 假定这是你的银行存款:
    balance = 0
    lock = threading.Lock()


    def change_it(n):
        # 先存后取，结果应该为0:
        global balance
        balance = balance + n
        balance = balance - n


    def run_thread(n):
        for i in range(100000):
            # 先要获取锁:
            lock.acquire()
            try:
                # 放心地改吧:
                change_it(n)
            finally:
                # 改完了一定要释放锁:
                lock.release()


    def run_thread(n):
        for i in range(100000):
            change_it(n)


    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)
    pass
    pass


    
    