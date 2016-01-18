#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

from flask import Flask
from flask import request,current_app,make_response,redirect,abort,render_template,session,url_for,flash
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
import os
#为shell命令注册一个make_context回调函数
from flask.ext.script import Shell,Manager
import sqlite3

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
bootstrap=Bootstrap(app)
moment = Moment(app)
manager = Manager(app)

app.config['SECRET_KEY'] = 'HARD TO GUESS'
#app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:\\'+os.path.join(basedir,'myapp.sqlite')
#D:\\JetBrains\\workspaces\\mp\\src\\flask_test\\myapp.sqlite

#conn = sqlite3.connect('myapp.db')

app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:\\'+os.path.join(basedir,'myapp.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

#basic
@app.route('/')
def index():
    #user_agent = request.headers.__getattribute__('User_Agent')
    return "<h1>HelloWorld!!!</h1>"

#show content based on input your need
@app.route('/user/<name>')
def user(name):
    return "<h1>Hello, %s!</h1>" % name

#show content for a request
@app.route('/req_content/')
def req_content():
    user_agent = request.headers.get('User-Agent')
    return "Your browser is %s " % user_agent

#show usecase for curent_app in Flask
@app.route('/current_app/')
def current_app():
    app_ctx = app.app_context()
    app_ctx.push()
    myappname = current_app.name
    return "your current_app.name is " % myappname

@app.route('/bad_req/')
def bad_req():
    return '<h1>Bad Request. </h1>',400

#set cookie use flask
@app.route('/setcookie/')
def setcookie():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('liugang5','40')
    return response

#web page redirect method
@app.route('/redirect')
def page_redirect():
    return redirect('http://www.sina.com.cn')

#use a function called abort to handle exception
@app.route('/user/<id>')
def get_user(id):
    #userid = load_user(id)
    if not user:
        abort(404)
    #return '<h1>Hello, %s </h1>' % user.name
    return render_template("user_bootstrap.html",id=id)

#define a form class
class NameForm(Form):
    name = StringField('What is your name?',validators=[Required()])
    submit = SubmitField('Submit')

#operation databases;
class Role(db.Model):
    #
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)

    def __repr__(self):
        return '<Role %r' % self.name

    users = db.relationship('User',backref='role')

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True)

    def __repr__(self):
        return '<User %r>' % self.username

    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

#add a context for shell command
def make_shell_context():
    return dict(app=app,db=db,User=User,Role=Role)

manager.add_command("shell",Shell(make_context=make_shell_context()))

@app.route('/myapp',methods=['GET','POST'])
def myapp():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        #old version
        #name = form.name.data

        #using session to save user information and alert a message if submit a name
        '''
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name')
        session['name'] = form.name.data
        return redirect(url_for('index'))
        form.name.data = ''
        '''

        #get user information from database
        #if user submit the form, the programe will be use the funcation called filter_by() to search the name in databases;\
        #the parameter called known will be writen the user's session to show welcome infor
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data=''
        return redirect('index')
    #return render_template('index.html',form=form,name=session.get('name'))
    return render_template('index.html',form=form,name=session.get('name'),known=session.get('known',False))

if __name__ == "__main__":
    #app.run(debug=True)
    manager.run()
    #pass