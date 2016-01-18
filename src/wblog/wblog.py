#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

import os
from flask import Flask,render_template,request,redirect,url_for
import sqlite3

# configuration
DATABASE = 'D:\JetBrains\workspaces\mp\src\wblog\flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)

app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()


if __name__ == "__main__":
    app.run()
    pass