#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

import os,io

lines = open("data.txt")

fields = (line.split() for line in lines)

print(sum(float(f[1]) * float(f[2]) for f in fields))

'''
if __name__ == "__main__":
    pass
'''