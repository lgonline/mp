#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

from flask import Flask
from flask import make_response

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response('<h1>this document carries a cookie!</h1>')
    response.set_cookie('answer','42')
    return response

@app.route('/redirect/url')
def redirect():
    #url = 'http://www.sina.com.cn'
    return redirect('https://www.baidu.com')

if __name__ == "__main__":
    app.run(debug=True)