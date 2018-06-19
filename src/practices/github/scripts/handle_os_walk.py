#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/19 15:37
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : handle_os_walk.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com

"""

"""

import os

def main():
    for root,dirs,files in os.walk(".",topdown=False):
        # for name in files:
        #     print(os.path.join(name))
        for name in dirs:
            print(os.path.join(root,name))

    print('root is :',root)
    print('dirs is : ',dirs)
    print('files is : ',files)

    pass


if __name__ == '__main__':
    main()
