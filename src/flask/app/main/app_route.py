#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = 'liugang5'

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h2>Hello</h2>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s</h1>' % name

if __name__ == "__main__":
    app.run(debug=True)
    pass