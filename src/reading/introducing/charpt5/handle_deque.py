#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: lgonline 
@license: Apache Licence  
@contact: lgonline@hotmail.com 
@site:  
@software: PyCharm 
@file: handle_deque.py 
@time: 11/3/17 11:10 PM 
"""

"""
deque是一种双端队列，具有栈和队列的特性，它可以从序列的任何一个端添加和删除项
函数popleft去掉最左边的项并返回该项，pop去掉最右边的项并返回该项。
从两边一直扫描到中间，只要两端的字符匹配，一直弹出直到到达中间
"""

def func(word):
    from collections import deque

    dq = deque(word)

    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False

        return True
    pass


class main():
    func('a')
    func('racecar')
    def __init__(self):
        pass


if __name__ == "__main__":
    main()
    pass  