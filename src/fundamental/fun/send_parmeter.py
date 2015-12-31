#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

a = [1,2,3,4,5]

def square(item):
    for i,x in enumerate(item):
        item[i] = x * x #update the value in here

    print(item)

'''
def mysquare(item):
    for i,x in item:
        item[i] = x * x
    print(item)

Traceback (most recent call last):
  File "D:/JetBrains/workspaces/mp/src/fundamental/fun/send_parmeter.py", line 20, in <module>
    mysquare(a)
  File "D:/JetBrains/workspaces/mp/src/fundamental/fun/send_parmeter.py", line 14, in mysquare
    for i,x in item:
TypeError: 'int' object is not iterable
'''

if __name__ == "__main__":
    #square(a)
    mysquare(a)