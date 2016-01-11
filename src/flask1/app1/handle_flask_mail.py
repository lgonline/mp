#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

from flask.ext.mail import Mail
from flask.ext.mail import Message
from flask.ext.wtf import Form
from flask import Flask,render_template
from wtforms.validators import Required
from wtforms import SubmitField,StringField
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
mail = Mail(app)

#function for send the email
app.config['MAIL_SERVER'] = 'smtp.mail.yahoo.com'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[FLASKY]'
app.config['FLASKY_MAIL_SENDER'] = 'Ethan Admin <gangliucsa@yahoo.com>'
app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')

app.config['SECRET_KEY'] = 'hard to guess string'

def send_email(to,subject,template,**kwargs):
    msg = Message(ap.config['FLASK_MAIL_SUBJECT_PREFIX']+subject,
                  sender=app.config['FLASKY_MAIL_SENDER'],recipients=[to])
    msg.body = render_template(template+'.txt',**kwargs)
    msg.html = render_template(template+'.html',**kwargs)
    mail.send(msg)

class NameForm(Form):
    name = StringField('What your are name?',validators=[Required()])
    send = SubmitField('send')

#entend index view to send the email
@app.route('/',methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query
    return



if __name__ == "__main__":
    app.run(debug=True)
    pass
