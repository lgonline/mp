#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

'''
在蓝本中定义的程序路由

在蓝本中编写视图函数主要有两点不同：
第一，和前面的错误处理程序一样，路由修饰器由蓝本提供；
第二，url_for() 函数的用法不同。url_for() 函数的第一个参数是路由的端点名，在程序的路由中，默认为视图函数的名字。
在蓝本中，Flask 会为蓝本中的全部端点加上一个命名空间，这样就可以在不同的蓝本中使用相同的端点名定义视图函数，而不会产生冲突。
命名空间就是蓝本的名字（Blueprint 构造函数的第一个参数），所以视图函数index() 注册的端点名是main.index，其URL 使用url_for('main.index') 获取。
'''

from datetime import datetime
from flask import render_template,session,redirect,url_for

from . import main
from .forms import NameForm
from  .. import db
from ..models import User

@main.route('/',methods=['GET','POST'])
def index():
    form = NameForm


'''
if __name__ == "__main__":
    pass
'''