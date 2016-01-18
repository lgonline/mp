#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

from flask import Flask

app = Flask(__name__)

path = app.root_path


if __name__ == "__main__":
    print(path)