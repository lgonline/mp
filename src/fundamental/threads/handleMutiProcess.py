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
from multiprocessing import Process

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


if __name__ == '__main__':
    createProcessUsingFork()
    # createProcessUsingMultiprocessing()
    pass 
    
    