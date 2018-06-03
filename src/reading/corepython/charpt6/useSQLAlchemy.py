#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: 330mlcc 
@license: Apache Licence  
@contact: lg_online@126.com 
@site:  
@software: PyCharm 
@file: useSQLAlchemy
@time: 18-5-30 下午9:18 
Description: 
"""

from distutils.log import warn as printf
from os.path import dirname
from random import randrange as rand
from sqlalchemy import Column, Integer,String,create_engine,exc,orm
from sqlalchemy.ext.declarative import declarative_base

db = {
    # 'mysql':'mysql://root@localhost/%s',dbname,
}

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    login = Column(String(NAMELEN))
    userid = Column(Integer,primary_key=True)
    projectid = Column(Integer)

    def __str__(self):
        # return ''.join(map(tformat))
        pass


if __name__ == '__main__':
    pass 
    
    