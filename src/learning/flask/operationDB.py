#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

from flask import Flask,request,render_template,session,redirect,url_for,flash

from flask.ext.wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import required
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime
from flask.ext.sqlalchemy import SQLAlchemy
import os

import sqlite3

app = Flask(__name__)
bootstrap = Bootstrap(app)
momnet = Moment(app)
app.config['SECRET_KEY'] = "hard to guess string"
#db = sqlite3.connect('../mydb.db')
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///'+os.path.join(basedir,'mydb.db')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('templates/404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('templates/500.html'), 500

@app.route('/',methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username = form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True

        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html',form=form,name=session.get('name'),known = session.get('known',False),current_time=datetime.utcnow())

class NameForm(Form):
    name = StringField('What is your name',validators=[required()])
    submit = SubmitField('Submit')


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True,index=True)
    def __repr__(self):
        return '<User %r>' % self.username
    #一对多关系，关系使用users 表中的外键连接了两行。添加到User 模型中的role_id 列被定义为外键，就是这个外键建立起了关系。传给db.ForeignKey() 的参数'roles.id' 表明，这列的值是roles 表中行的id 值。
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

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

if __name__ == "__main__":
    app.run(debug=True)