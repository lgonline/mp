#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/20 12:01
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : random_name_generator.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com

"""
choice() 方法返回一个列表，元组或字符串的随机项。
"""

from random import choice

first_names = ["Drew", "Mike", "Landon", "Jeremy", "Tyler", "Tom", "Avery"]
last_names = ["Smith", "Jones", "Brighton", "Taylor"]
random_names = []

def main(first_name,last_name,x):
    for i in range(x):
        # random_names.append('{0} {1}'.format(choice(first_name),choice(last_name)))
        random_names.append('{0} {1}'.format(choice(first_name),choice(last_name)))
    return set(random_names)
    pass


if __name__ == '__main__':
    random_names = main(first_names,last_names,5)
    print('\n'.join(random_names))
