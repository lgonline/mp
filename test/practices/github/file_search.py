#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/19 16:17
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : file_search.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com

"""

"""

import os,fnmatch

PATH = '.'
pattern = '*.py'

def main(filepath,pattern):
    filelists = []
    if os.path.exists(filepath):
        for root,dirs,filenames in os.walk(filepath):
            for filename in fnmatch.filter(filenames,pattern):
                filelists.append(filename)
        if filelists:
            print(print('{} files was found.'.format(len(filelists))))
            for file in filelists:
                print(root,file)
        pass
    else:
        print('the file you wanted is not found')
    pass


if __name__ == '__main__':
    main(PATH,pattern)
