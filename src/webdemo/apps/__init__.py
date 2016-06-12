#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = 'liugang5'

from flask import Flask

app = Flask(__name__)

from webdemo.apps import views

if __name__ == "__main__":
    pass