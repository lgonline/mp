#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/12 21:12
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : rename_with_slice.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com

import os
import glob



def main():
    os.chdir("d:\\")

    for file in glob.glob("*.jpg"):
        file_name = os.path.splitext(file)[0]
        extension = os.path.splitext(file)[1]
        print(file_name)
        print(extension)
        new_file_name = file_name[:-6] + extension
        print(new_file_name)

        try:
            os.rename(file,new_file_name)
        except OSError as e:
            print(e)
        else:
            print("Renamed {} to {}".format(file,new_file_name))
    pass


if __name__ == '__main__':
    main()
