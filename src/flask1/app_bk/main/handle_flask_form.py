#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

from flask import Flask,render_template,session,redirect,url_for,flash
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'hard to guess string'

class NameForm(Form):
    name = StringField('What is your name.', validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        #a normal method for get data form web form
        '''
        name = form.name.data
        form.name.data = ''
        '''

        #redirect user session to fix the some confirm message whe user submit the form
        #name was stored on user session, rather than was stored in parameter, so the name can be keep in two dialog
        '''
        session['name'] = form.name.data
        return redirect(url_for('index'))
        '''

        #updated function to meet requirement that alert some messges if it have any error.
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))

    #a normal method fo rget data form web form
    #return render_template('index_for_form.html',form=form,name=name)
    return render_template( '/templates/index_for_form.html',form=form,name=session.get('name'))

if __name__ == "__main__":
    app.run(debug=True)
    pass