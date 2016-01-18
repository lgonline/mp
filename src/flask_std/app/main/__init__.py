#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

'''
蓝本中定义的路由处于休眠状态，蓝本注册到程序上后，路由才真正成为程序的一部分。
使用位于全局作用域中的蓝本时，定义路由的方法几乎和单脚本程序一样。
'''
#通过实例化一个Blueprint 类对象可以创建蓝本。这个构造函数有两个必须指定的参数：蓝本的名字和蓝本所在的包或模块。
from flask import Blueprint
main = Blueprint('main', __name__)
#程序的路由保存在包里的app/main/views.py 模块中，而错误处理程序保存在app/main/errors.py 模块中。
# 导入这两个模块就能把路由和错误处理程序与蓝本关联起来。
from . import errors,views

'''
if __name__ == "__main__":
    pass
'''