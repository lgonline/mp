#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

from flask import Flask

#define a web form class
#from flask.ext.wtf import Form
#from wtforms import *
#from wtforms import StringField,SubmitField
#from wtforms.validators import DataRequired
#from flask import Flask,render_template


from flask.ext.wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required
from flask import Flask,render_template


app = Flask(__name__)

class NameForm():
    name = StringField('What is your name?',validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('form_index.html',form=form,name=name)


if __name__ == "__main__":
    app.run(debug=True)