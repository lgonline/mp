#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

from flask import Flask
from flask import request,current_app,make_response,redirect,abort

app = Flask(__name__)

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
    return '<h1>Hello, %s </h1>' % user.name

if __name__ == "__main__":
    app.run(debug=True)
    pass