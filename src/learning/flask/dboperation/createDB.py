#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

#import sqlite3

import os
import sqlite3
from src.learning.flask.dboperation.table_structure import Role,User
from flask import Flask

from flask.ext.sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'mydb.db')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

if __name__ == "__main__":
    '''
    conn = sqlite3.connect('../mydb.db')
    cursor = conn.cursor()

    create_table_sql1 = """
    create table if not exists User(
      id INTEGER PRIMARY KEY autoincrement UNIQUE not null,
      name varchar(100)
    );
    """
    create_table_sql2 = """
    create table if not exists Role(
      id INTEGER PRIMARY KEY autoincrement UNIQUE not null,
      username varchar(100)
    );
    """

    cursor.execute(create_table_sql1)
    cursor.execute(create_table_sql2)

    conn.commit()
    '''

    class Role(db.Model):
        __tablename__ = 'roles'
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(64), unique=True)
        def __repr__(self):
            return '<Role %r>' % self.name

        users = db.relationship('User', backref='role')

    class User(db.Model):
        __tablename__ = 'users'
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(64), unique=True, index=True)
        def __repr__(self):
            return '<User %r>' % self.username

        role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    db.create_all()
