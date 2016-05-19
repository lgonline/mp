#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = 'liugang5'

from flask import Flask,render_template,url_for,request
#以用 url_for() 来给指定的函数构造 URL。它接受函数名作为第一个参数，也接受对应 URL 规则的变量部分的命名参数。未知变量部分会添加到 URL 末尾作为查询参数。

#使用Flask-Script支持命令行选项，Flask-Script 是一个Flask 扩展，为Flask 程序添加了一个命令行解析器。Flask-Script 自带了一组常用选项，而且还支持自定义命令。
from flask.ext.script import Manager

app = Flask(__name__)
#manager = Manager(app)

@app.route('/')
def index():
    return '<h1>Hello, liugang5</h1>'

@app.route('/user/')
def user(name):
    return render_template('user.html',name=name)

@app.route('/login',method=['GET','POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()

@app.route('/user/<username>')
def profile(username): pass

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login',next='/'))
    print(url_for('profile',username='liugang5'))

if __name__ == "__main__":
    app.run(debug=True)
    #manager.run()