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
@file: execution_time.py
@time: 18-6-13 下午10:44 
Description: 
"""

import time
import random

class ExecutionTime:
    def __init__(self):
        self.start_time = time.time()

    def duration(self):
        print(time.time())
        print(self.start_time)
        return time.time() - self.start_time

def main():
    timer = ExecutionTime()
    sample_list = list()
    my_list = [random.randint(1,888898) for num in range(1,1000000) if num % 2 == 0]
    # for lists in my_list:
    #     print(lists)
    print('hello world!')
    print('Finished in {} seconds.'.format(timer.duration()))
    pass


if __name__ == '__main__':
    main()
    pass 
    
    