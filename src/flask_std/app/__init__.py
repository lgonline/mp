#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from src.flask_std.config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

'''
#create_app() 函数是程序的工厂函数，接受一个参数，是程序使用的配置名。
# 配置类在config.py 文件中定义，其中保存的配置可以使用Flask app.config 配置对象提供的from_object() 方法直接导入程序。
# 至于配置对象，通过名字从config 字典中选择。程序创建并配置好后，就能初始化扩展了。
# 在之前创建的扩展对象上调用init_app() 可以完成初始化过程。
'''

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    # 附加路由和自定义的错误页面

    #蓝本在工厂函数create_app() 中注册到程序上
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app