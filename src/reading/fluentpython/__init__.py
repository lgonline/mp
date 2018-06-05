#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = '330mlcc'

theBoard = {'top-L':'','top-M':'','top-R':'','mid-L':'','mid-M':'','mind-R':'','low-L':'','low-L':'','low-M':'','low-R':''}

def printBoard(board):
    print(board['top-L':'|','top-M':'|','top-R':''])
    print('-+-+-}')

    for i in range(9):
        printBoard(theBoard)

if __name__ == '__main__':
    pass

