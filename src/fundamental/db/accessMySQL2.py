__author__ = 'Administrator'

import pymysql

conn = pymysql.Connection(host='127.0.0.1',user='root',passwd='123456')
cur = conn.cursor()

try:
    cur.execute("drop database mpdb")
except Exception as e:
    print(e)
finally:
    pass

cur.execute("create database mpdb")
cur.execute("use mpdb")

cur.execute("create table users(id int,name varchar(8))")
cur.execute("insert into users values(1,'www'),(2,'cnblogs'),(3,'com'),(4,'peter')")

cur.execute('select * from users')
for row in cur.fetchall():
    print(row)

cur.close()
conn.commit()
conn.close()