#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

from werkzeug.security import generate_password_hash,check_password_hash
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

password_hash = db.Column(db.String(128))

@property
def password(self):
    raise AttributeError('Password is not a readable attribute')

@password.setter
def password(self,password):
    self.password_hash = generate_password_hash(password)

def verify_password(self,password):
    return check_password_hash(self.password_hash,password)

if __name__ == "__main__":
    pass