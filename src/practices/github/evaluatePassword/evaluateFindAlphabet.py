#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/8 15:26
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : evaluateFindAlphabet.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com

"""

"""


import re

def evaluateFindAlphabet(line):
    mode = re.compile('[a-z]+')
    str = line
    return mode.findall(str)