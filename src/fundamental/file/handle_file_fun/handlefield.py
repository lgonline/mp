#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

import os

parent_path, name = os.path.split("c:\\logs\\2012\\12\\15")

def split_fully(path):
    my_parent_path,my_name = os.path.split(path)
    if my_name == '':
        return (my_parent_path,)
    else:
        return split_fully()

if __name__ == "__main__":
    print(parent_path)
    print(name)