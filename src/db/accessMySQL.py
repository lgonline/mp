__author__ = 'Administrator'

import os,sys
import pymysql

try:
    conn = pymysql.connect(host='localhost',user='root',passwd='lgonline',db='bm',port=3306,charset='utf8')
    cur=conn.cursor()
    cur.execute('select userid,name,password from userinfo')
    data=cur.fetchall()
    for d in data:
        print("userid: "+str(d[0])+' name: '+d[1]+" password: "+d[2])

    cur.close()
    conn.close()
except Exception:
    print("the exception was throw.")