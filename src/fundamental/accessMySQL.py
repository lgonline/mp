__author__ = 'Administrator'

import os,sys
import pymysql

def sampleConnMysql():
    try:
        conn = pymysql.connect(host='localhost',user='root',passwd='123456',db='bm',port=3306,charset='utf8')
        cur=conn.cursor()
        cur.execute('select userid,name,password from userinfo')
        data=cur.fetchall()
        for d in data:
            print("userid: "+str(d[0])+' name: '+d[1]+" password: "+d[2])

        cur.close()
        conn.close()
    except Exception:
        print("the exception was throw.")


def connMySQLDemo():
    import pymysql

    conn = pymysql.Connection(host='127.0.0.1', user='root', passwd='123456')
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

if __name__ == '__main__':
    pass