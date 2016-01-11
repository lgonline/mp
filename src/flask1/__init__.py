#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

'''
在单个文件中开发程序很方便，但却有个很大的缺点，因为程序在全局作用域中创建，所以无法动态修改配置。
运行脚本时，程序实例已经创建，再修改配置为时已晚。这一点对单元测试尤其重要
这个问题的解决方法是延迟创建程序实例，把创建过程移到可显式调用的工厂函数中。这种方法不仅可以给脚本留出配置程序的时间，
还能够创建多个程序实例

构造文件导入了大多数正在使用的Flask 扩展。由于尚未初始化所需的程序实例，所以没有初始化扩展，创建扩展类时没有向构造函数传入参数。
create_app() 函数就是程序的工厂函数，接受一个参数，是程序使用的配置名。
配置类在config.py 文件中定义，其中保存的配置可以使用Flask app.config 配置对象提供的from_object() 方法直接导入程序。
至于配置对象，则可以通过名字从config 字典中选择。程序创建并配置好后，就能初始化扩展了。在之前创建的扩展对象上调用init_app() 可以完成初始化过程。
'''

from flask import Flask,render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from flask1.config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

'''
if __name__ == "__main__":
    pass
'''