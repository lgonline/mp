#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 17:30
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : countFolde.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com

"""
获取当前文件夹下的所有文件
"""

import os

results = []

def get_all_folde(cwd):
    get_dir = os.listdir()  #遍历当前目录，获取文件列表
    print(get_dir)
    for i in get_dir:
        # 把第一步获取的文件加入路径
        sub_dir = os.path.join(cwd,i)
        print(sub_dir)
        # 如果当前仍然是文件夹，递归调用
        if os.path.isdir(sub_dir):
            get_all_folde(sub_dir)
        else:
            # 如果当前路径不是文件夹，则把文件名放入列表
            ax = os.path.basename(sub_dir)
            results.append(ax)
            # 对列表计数
            print(len(results))

if __name__ == '__main__':
    # 当前目录
    cur_path = os.getcwd()
    print(cur_path)
    get_all_folde(cur_path)
