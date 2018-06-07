#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 17:38
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : get_current_files.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com

"""

"""

import os

results = []

def get_current_file(cwd):
    current_folder1 = os.getcwd()
    print(current_folder1)
    current_folder = os.listdir()
    print(current_folder)
    for i in current_folder:
        sub_folder = os.path.join(cwd,i)
        if os.path.isdir(sub_folder):
            get_current_file(sub_folder)
        else:
            filename = os.path.basename(sub_folder)
            results.append(filename)
            print(len(results))
    pass


if __name__ == '__main__':
    # cwd = os.getcwd()
    # get_current_file(cwd)
    print(os.getcwd())
    print(os.listdir())
