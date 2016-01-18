#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

from flask.ext.wtf import Form
from wtforms import SubmitField,StringField
from wtforms.validators import Required

class NameForm(Form):
    name = StringField('What your are name?',validators=[Required()])
    submit = SubmitField('submit')