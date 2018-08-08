#!/usr/bin/env python  
# -*- coding: utf-8 -*-

""" 
@version: v1.0 
@author: 330mlcc 
@Software: PyCharm
@license: Apache Licence  
@Email   : mlcc330@hotmail.com
@contact: 3323202070@qq.com
@site:  
@software: PyCharm 
@file: handelMySQL.py
@time: 18-7-22 下午3:04 
Description: 
"""

import pymysql,os

def main():
    try:
        conn = pymysql.connect(host='localhost',user='root',passwd='toor',db='mpdb',port=3306)
        cur = conn.cursor()
        cur.execute('select * from test')

        results = cur.fetchall()
        for result in results:
            print(result)

        cur.close()
        conn.close()
    except pymysql.Error as e:
        print(e)
    pass


if __name__ == '__main__':
    main()
    pass 
    
    