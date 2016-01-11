#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors

if __name__ == "__main__":
    pass