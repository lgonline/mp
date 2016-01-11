#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

from flask import Flask,render_template
from flask.ext.moment import Moment
from flask.ext.bootstrap import Bootstrap
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    return render_template('localtime_index.html', current_time=datetime.utcnow())

if __name__ == "__main__":
    app.run(debug=True)
    pass