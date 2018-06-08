#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/8 15:31
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : evaluateFindNum.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com

"""

"""

import re

def evaluateFindNum(line):
    mode = re.compile(r'\d+')
    str = line
    return mode.findall(str)