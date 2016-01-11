#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

#基类Config 中包含通用配置，子类分别定义专用的配置。如果需要，还可添加其他配置类。
class Config:
    #SECRET_KEY 的值，这是个敏感信息，可以在环境中设定，但系统也提供了一个默认值，以防环境中没有定义。
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALECHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Ethan Admin <gangliucsa@yahoo.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.yahoo.com.cn'
    MAIL_PORT = '465'
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URL = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///'+os.path.join(basedir,'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URL = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///'+os.path.join(basedir,'data-dev.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URL = os.environ.get('PRO_DATABASE_URL') or \
        'sqlite:///'+os.path.join(basedir,'data-dev.sqlite')

#，config 字典中注册了不同的配置环境，而且还注册了一个默认配置（本例的开发环境）。
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}