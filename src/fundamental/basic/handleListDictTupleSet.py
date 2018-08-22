#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/21 12:15
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : handleListDictTupleSet.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com
# @Description: 
#   
#

from random import randint

def handleDict():
    userDictionary = {}
    for i in range(10):
        for j in range(i + 1):
            j += 10
            # pass
        userDictionary.setdefault(i, j)
    print(userDictionary)

    del (userDictionary[0])
    print(userDictionary)

    userDictionary.pop(1)
    print(userDictionary)

    for (k, v) in userDictionary.items():
        print(k, ":", v)
    # 遍历
    print(userDictionary.items())

    # 拷贝
    copyUserDictionary = userDictionary.copy()
    print(copyUserDictionary)

    print(copyUserDictionary.get(3))


def handleLists():
    allnums = [1, 2, 3, 4, 5]
    allnums[0] = 6
    print(allnums)

def handleSets():
    items = ['dcy', 'admin', 'mxl', 'another', 'happy', 'sorry']
    i = 1
    while i <= 1:
        i += 1
        print("---------starting-------")
        for danqu in items:
            if danqu == 'sorry':
                break
            if danqu == 'admin':
                continue

            print(" the ", i - 1, ' times to show the name is ; ', danqu)

def handleDataType():
    int_type = 4
    string_type = "hello"
    tuple_type = (1, 2, 3, 4, 5, 6, 7, 8)
    list_type = ['a', 'b', 'c', 'd']
    dict_type = {'key1': 'aaa', 'key2': 'bbb', 'key3': 'ccc'}

    print('the type of int_type is ', type(int_type), ', and the value is ', int_type)
    print('the type of int_type is ', type(string_type), ', and the value is ', string_type)
    print('the type of int_type is ', type(tuple_type), ', and the value is ', tuple_type)
    print('the type of int_type is ', type(list_type), ', and the value is ', list_type)
    print('the type of int_type is ', type(dict_type), ', and the value is ', dict_type)

def generateRandom():
    allnums = []
    for i in range(10):
        allnums.append(randint(1000, 9999))
    print("add component is : ", allnums)

    for j in range(len(allnums)):
        print("remove component is : ", allnums.pop())

def main():
    handleDataType()
    pass


if __name__ == '__main__':
    main()
    pass