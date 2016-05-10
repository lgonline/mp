#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

import pymysql

if __name__ == "__main__":
    conn = pymysql.connect(user='root',passwd='lgonline',host='localhost',db='mm')

    cur = conn.cursor()

    cur.execute("select * from test")

    for i in cur:
        print("row_number"+str(cur.rownumber))
        print("id is : "+str(i[0])+", name is : "+str(i[1]))

    cur.close()
    conn.close()

    pass