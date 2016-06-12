#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = 'liugang5'

from mw.apps1 import app

@app.route('/')
@app.route('/index')
def index():
    return "<h1>Hello World!!!</h1>"

if __name__ == "__main__":
    pass