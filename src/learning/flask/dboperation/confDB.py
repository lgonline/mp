#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

'''程序使用的数据库URL 必须保存到Flask 配置对象的SQLALCHEMY_DATABASE_URI 键中。配置对象中还有一个很有用的选项，即SQLALCHEMY_COMMIT_ON_TEARDOWN 键，将其设为True时，每次请求结束后都会自动提交数据库中的变动。'''
app.config['SQLALCHEMY_DATABASE_URL'] = 'D:\\JetBrains\\workspaces\\mp\\src\\learning\\flask\\blog.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

'''
在ORM 中，模型一般是一个Python 类，类中的属性对应数据库表中的列。
角色到用户的一对多关系，因为一个角色可属于多个用户，而每个用户都只能有一个角色。
'''
class Role(db.Model):
    #定义在数据库中使用的表名,如果没有定义__tablename__，Flask SQLAlchemy 会使用一个默认名字,但默认的表名没有遵守使用复数形式进行命名的约定
    __tablename__ = 'roles'
    #db.Column 类构造函数的第一个参数是数据库列和模型属性的类型
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    #定义了__repr()__ 方法，返回一个具有可读性的字符串表示模型，可在调试和测试时使用。
    def __repr__(self):
        return '<Role %r>' % self.name
    #添加到Role 模型中的users 属性代表这个关系的面向对象视角。对于一个Role 类的实例，其users 属性将返回与角色相关联的用户组成的列表。db.relationship() 的第一个参数表明这个关系的另一端是哪个模型。如果模型类尚未定义，可使用字符串形式指定。
    #db.relationship() 中的backref 参数向User 模型中添加一个role 属性，从而定义反向关系。这一属性可替代role_id 访问Role 模型，此时获取的是模型对象，而不是外键的值。
    users = db.relationship('User',backref='role')

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True,index=True)
    def __repr__(self):
        return '<User %r>' % self.username
    #一对多关系，关系使用users 表中的外键连接了两行。添加到User 模型中的role_id 列被定义为外键，就是这个外键建立起了关系。传给db.ForeignKey() 的参数'roles.id' 表明，这列的值是roles 表中行的id 值。
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

if __name__ == "__main__":
    app.run(debug=True)
    pass