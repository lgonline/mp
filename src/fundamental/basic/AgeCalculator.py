#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = '330mlcc'


def checkAge(oldage,furtherage,realage):
    diffage = (int)(furtherage - oldage)
    realage = (int)(realage + diffage)
    print('diffage is ', diffage, ' and realage is : ', realage)
    # return realage

def calculator():
    flag = True;
    lists = ['+','-','*','/']
    while flag:
        theOne = int(input("please input that your first numbers :"))
        theSecond = int(input("please input that your second numbers :"))
        symbol = input("please input your want method : (+,-,*,/)")

        if symbol in lists:
            if symbol == "+":
                print(theOne, "+", theSecond, "=", theOne + theSecond)
            elif symbol == '-':
                print(theOne, "-", theSecond, "=", theOne - theSecond)
            elif symbol == '*':
                print(theOne, "*", theSecond, "=", theOne * theSecond)
            elif symbol == '/':
                if theSecond == 0:
                    print("your second number input is not zero")
                    continue
                else:
                    print(theOne, "/", theSecond, "=", theOne / theSecond)
        else:
            print('您输入的不是一个合法的数据操作.')
            continue
        print("Do your want to end this calculate?(Y/N)")
        operation = input("")
        if operation == 'y' or operation =='Y':
            print("the programe is exist!")
            break
        else:
            continue

def printAdditionTable():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(i, "+", j, "=", i + j, "\t", end="")
        print('\n')

def printMultiplicationTable():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(i, "*", j, "=", i * j, "\t", end="")
        print('\n')

def guestDemo():
    target = 60

    while True:
        value = input("enter an integer between 1 and 100. \n")
        try:
            value = int(value)
            break
        except ValueError:
            print('i said enter an integer!')

    if value > target:
        print(value, " is too high")
    elif value < target:
        print(value, ' is too low')
    else:
        print('pefect')

if __name__ == '__main__':
    printMultiplicationTable()