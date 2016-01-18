#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

from flask.ext.mail import Mail
from flask.ext.mail import Message
from flask import Flask,render_template
from threading import Thread

app = Flask(__name__)
mail = Mail(app)


def send_sync_email(app,msg):
    with app.app_context():
        mail.send(msg)

def send_email(to,subject,template,**kwargs):
    msg = Message(app.config['FLASK_MAIL_SUBJECT_PREFIX']+subject,
                  sender=app.config['FLASKY_MAIL_SENDER'],recipients=[to])
    msg.body = render_template(template+'.txt',**kwargs)
    msg.html = render_template(template+'.html',**kwargs)
    thr = Thread(target=send_sync_email, args=[app, msg])
    thr.start()
    return thr