#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/4 19:32
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : handle_os_path.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com
# @Description: 
#   
#   

import os

def main():
    print('os.path.abspath(__file__) is : ',os.path.abspath(__file__))
    print('os.path.abspath(".") is : ', os.path.abspath('.'))
    print(os.listdir(os.path.abspath('.')))
    print(os.path.isdir(os.path.abspath('.')))
    print(os.path.exists(os.path.abspath('.')))
    pass


if __name__ == '__main__':
    main()
    pass