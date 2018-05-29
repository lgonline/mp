#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

'''
    目标：文本块生成器，把文本切分成段落，段落被一个或多个空行隔开。
    解决思路：遇到一个空行，然后返回已经收集的行，即一个块；之后，再次开始收集
'''

def lines(file):
    for line in file:
        yield line
        yield "\n"

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield "".join(block).strip()
            block = []

if __name__ == "__main__":
    pass