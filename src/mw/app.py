#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = 'liugang5'

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Wrold!"

if __name__ == "__main__":
    app.run()