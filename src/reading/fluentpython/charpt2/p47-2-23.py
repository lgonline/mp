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
@file: p47-2-23.py
@time: 18-8-29 下午11:11 
Description: 
"""

from collections import deque

def useDequeMethod():
    '''
    append和pop方法可以把列表当作栈或者队列使用，但添加或删除第一个元素很耗时
    Collections.deque是一个线程安全、快速从两端删除、添加的数据类型
    '''
    dq = deque(range(10),maxlen=10)
    print('dq is : ',dq)
    dq.rotate(3)
    print('execute dq.rotate(3) is : ',dq)
    dq.rotate(-4)
    print('execute dq.rotate(-4) is : ', dq)
    dq.appendleft(-1)
    print('execute dq.append(-1) is : ',dq)


def main():
    useDequeMethod()
    pass


if __name__ == '__main__':
    main()
    pass 
    
    