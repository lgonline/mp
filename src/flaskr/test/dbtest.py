#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

#all the imports
import sqlite3
from flask import Flask,request,session,g,redirect,url_for,abort,render_template,flash

#configuration
DATABASE = 'D:\\jETbRAINS\\workspaces\\mp\\flasker\\testdb.db'
#DEBUG 标志用于开关交互调试器。因为调试模式允许用户执行 服务器上的代码，所以 永远不要在生产环境中打开调试模式 ！
DEBUG = True
#secret_key （密钥）用于保持客户端会话安全，请谨慎地选择密钥，并尽可能的使它 复杂而且不容易被猜到。
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

#create a real application and init it via configuration

app = Flask(__name__)
'''
from_object() 会查看给定的对象（如果该对象是一个字符串就会 直接导入它），搜索对象中所有变量名均为大字字母的变量。
在我们的应用中，已经将配 置写在前面了。你可以把这些配置放到一个独立的文件中。
'''
app.config.from_object(__name__)

if __name__ == "__main__":
    pass