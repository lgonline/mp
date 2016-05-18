#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = 'liugang5'

from flask import Flask,render_template

#使用Flask-Script支持命令行选项，Flask-Script 是一个Flask 扩展，为Flask 程序添加了一个命令行解析器。Flask-Script 自带了一组常用选项，而且还支持自定义命令。
from flask.ext.script import Manager

app = Flask(__name__)
#manager = Manager(app)

@app.route('/')
def index():
    return '<h1>Hello World!!!</h1>'

@app.route('/user')
def user(name):
    return render_template('user.html',name=name)

if __name__ == "__main__":
    app.run(debug=True)
    #manager.run()