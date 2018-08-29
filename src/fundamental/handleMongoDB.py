#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/9 11:40
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : handleMongoDB.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com
# @Description: 
#   
#   
import sys
import os
os.chdir('.')
sys.path.append('.')

from pymongo import MongoClient
from fundamental.db.db_config import *

DATABASE_IP = '127.0.0.1'
DATABASE_PORT = 6379
DBUSER = 'aaa'
DBPASS = 'aaa'
DATABASE_NAME = 'aaa'

def conn_db():
    try:
    # 创建连接对象
        client = MongoClient(DATABASE_IP, DATABASE_PORT)
        db_auth = client.admin
        db_auth.authenticate(DBUSER, DBPASS)

        # 获取数据库
        target_db = client[DATABASE_NAME]
    except Exception as e:
        print(e)

    return target_db

def insert_db(db,key,value):
    try:
        db.stu.insert_one({"name": key, "app": value})
    except Exception as e:
        print(e)

def search_db(db,conditions):
    try:
        res = db.test.find_one({"name":conditions})
        print(res)
    except Exception as e:
        print(e)

def main():
    # 创建连接对象
    # client = MongoClient(DATABASE_IP,DATABASE_PORT)
    # db_auth = client.admin
    # db_auth.authenticate(DBUSER,DBPASS)

    # 获取数据库
    # target_db = client[DATABASE_NAME]

    # 向stu集合插入数据
    # target_db.stu.insert_one({"name":"liugang9","app":"jd"})

    # collection = target_db.stu
    # print(list(collection.find({'name':'root'})))
    # print(target_db.collection_names())

    databses = conn_db()
    # insert_db(databses,'ccc','ddd')
    # search_db(databses,'aaa')

    for id in range(0,100):
        insert_db(databses,("test"+str(id)),("name"+str(id)))

    pass


if __name__ == '__main__':
    main()
    pass