#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = 'liugang5'

#编写程序，用户输入一个三位以上的整数，输出其百位以上的数字。例如用户输入1234，则程序输出12
def handle_input():
    inputs = int(input('Please input an integer of more than 3 digits.'))
    try:
        inputs = inputs // 100
        if inputs == 0:
            print('You must input an integer of more than 3 digits.')
        else:
            print(inputs)
    except BaseException:
        print('you must input an integer')

#有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少
def MedleyNumer():
    for i in range (1,5):
        for j in range (1,5):
            for k in range (1,5):
                if (i != k) and (i!=j) and (k!=j):
                    print(i,j,k)

if __name__ == "__main__":
    #handle_input()
    MedleyNumer()