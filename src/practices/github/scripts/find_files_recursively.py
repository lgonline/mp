#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/19 10:40
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : find_files_recursively.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com

"""
使用递归方法在文件夹中查找指定类型的文件
"""

import os,fnmatch

PATH = '.'
Targets = '*.py'

def main(filepath,pattern):
    matches = []
    if os.path.exists(filepath):
        for root,dirnames,filenames in os.walk(filepath):
            for filename in fnmatch.filter(filenames,pattern):
                matches.append(os.path.join(filename))

            if matches:
                print('found {} files'.format(len(matches)))
                output_files(matches)

            else:
                print('no files found.')
    else:
        print('sorry that path does not exist,try again.')


def output_files(list_of_files):
    for filename in list_of_files:
        print(filename)

    pass


if __name__ == '__main__':
    main(PATH,Targets)
