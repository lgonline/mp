#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

import os
import re

def printENV():
    # 将正则表达式编译成Pattern对象
    pattern = re.compile(r";")

    for contents in pattern.split(os.environ["PATH"]):
        print(contents)

if __name__ == "__main__":
    printENV()