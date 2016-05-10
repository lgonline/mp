#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect('mydb.db')
    cursor = conn.cursor()

    search_sql = 'select * from users'
    search_sql2 = 'select * from roles'

    cursor.execute(search_sql)
    cursor.execute(search_sql2)

    data_set1 = cursor.fetchall()
    data_set2 = cursor.fetchall()

    for row1 in data_set1:
        print(row1)

    for row2 in data_set2:
        print(row2)

    cursor.close()
    conn.close()

