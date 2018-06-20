#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/8 15:33
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : evaluateSpecialWord.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com

"""

"""

import re

def evaluateSpecialWord(line):
    mode = re.compile(r'\W+')
    str = line
    return mode.findall(str)
