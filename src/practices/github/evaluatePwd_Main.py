#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/8 15:08
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : evaluatePwd_Main.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com

# import sys
# import os
# base_dir = os.path.abspath(__file__)
# sys.path.append(base_dir)

# from practices.github.evaluatePwd_Tools import readFile
# from .evaluatePwd_Tools import readFile
# from ..github.evaluatePwd_Tools import *
# from ..github.evaluateFindAlphabet import *
# from ..github.evaluateSpecialWord import *
# from ..github.evaluateFindNum import *
# import math

def saveFile(dict_name):
    f = open('temp.txt','w')
    f.write(str(dict_name))
    f.close()

def readFile():
    f = open('temp.txt','r')
    a = f.read()
    return eval(a)
    # return eval(a)

if __name__ == '__main__':
    maxList = readFile()
    print(maxList)
    # for m in maxList:
    #     print(m)
    #for aaa in maxList:
    #    print(aaa)
    # print(maxList[1]['q']/sum(maxList[1].values()))
    # testPassword = input('please enter your passwd your wanted.\n')
    # pwdWrods = {}
    #
    # for str in evaluateFindAlphabet(testPassword):
    #     if str in maxList[len(str)].keys():
    #         pwdWrods[str] = maxList[len(str)][str]/sum(maxList[len(str)].values())
    #     else:
    #         pwdWrods[str] = 1
    #
    # for str in evaluateFindNum(testPassword):
    #     if str in maxList[len(str)].keys():
    #         pwdWrods[str] = maxList[len(str)][str] / sum(maxList[len(str)].values())
    #     else:
    #         pwdWrods[str] = 1
    #
    # for str in evaluateSpecialWord(testPassword):
    #     if str in maxList[len(str)].keys():
    #         pwdWrods[str] = maxList[len(str)][str] / sum(maxList[len(str)].values())
    #     else:
    #         pwdWrods[str] = 1
    #
    # print(pwdWrods)
    #
    # P =1
    #
    # for i in pwdWrods.values():
    #     p *= i
    #
    # P = -math.log(P)
    # print(P)
    pass