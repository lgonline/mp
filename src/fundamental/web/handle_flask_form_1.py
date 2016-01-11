#!/usr/bin/python
#-*- coding: utf-8 pp-*-
__author__ = 'liugang5'

from flask import Flask

#define a web form class
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required
from flask import Flask,render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)

class NameForm(Form):
    name = StringField('What is your name?',validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('wtf_index.html',form=form,name=name)

if __name__ == "__main__":
    app.run(debug=True)