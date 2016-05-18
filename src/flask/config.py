#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = 'liugang5'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

#基类Config 中包含通用配置
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[fLASKY]'
    FLASK_MAIL_SENDER = 'Flasky Admin <lg_online@126.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass

#子类分别定义专用的配置
class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.126.com'
    MAIL_PORT =
    MAIL_USERNAME =
    MAIL_PASSWORD =
    SQLALCHEMY_DATABASE_URL =

#子类分别定义专用的配置
class TestingConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URL =

#子类分别定义专用的配置
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URL =

#config 字典中注册了不同的配置环境，而且还注册了一个默认配置
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

if __name__ == "__main__":
    #print(basedir)
    pass