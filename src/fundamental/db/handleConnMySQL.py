#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'Administrator'

#import MySQL drivers
import pymysql

conn = pymysql.connect(user='root',password='toor',database='test')
cursor = conn.cursor()

#create table
cursor.execute('create table user(id VARCHAR(20) PRIMARY key,name VARCHAR (20))')
#insert a data
cursor.execute('insert into user (id,name) values(%s,%s)',['1','Michael'])
print('The ',cursor.rowcount,' row in this database')

conn.commit()
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from user where id = %s',['1'])
values = cursor.fetchall()
print('my values is ',values)