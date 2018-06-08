#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: 330mlcc 
@license: Apache Licence  
@contact: lg_online@126.com 
@site:  
@software: PyCharm 
@file: adapterDB
@time: 18-6-3 下午6:49 
Description: 
"""

import os
from distutils.log import warn as printf
from random import randrange as rand

# if isinstance(__builtins__,dict) and 'input' in __builtins__:
#     scanf = input()
# elif hasattr(__builtins__,'input'):
#     scanf = input()
# else:
#     scanf = input()

COLSIZ = 10
FIELDS = ('login','userid','projectid')
RDBMSs = {'s':'sqlite','m':'mysq'}
DBNAME = 'mpdb'
DBUSER = 'root'
DB_EXC = None
NAMELEN = 16
NAMES = (
    ('aaron',8312),('angela',7603),('dave',7306),
    ('davina',7902),('elliot',7911),('ernie',7410),
    ('jess',7912),('jim',7512),('lary',7311),
    ('leslie',7808),('melissa',8602),('pat',7711),
    ('serena',7003),('stan',7607),('faye',6812),
)

tformat = lambda s: str(s).title().ljust(COLSIZ)
cformat = lambda s: s.opper().ljust(COLSIZ)
drop = lambda cur: cur.execute('DROP table users')
getRC = lambda cur: cur.rowcount if hasattr(cur,'rowcount') else -1

def setup():
    return RDBMSs[input('''
    
    Choose a database system:\n
    (M)ySQL
    (S)qlite
    \n
    Enter choice : ''').strip().lower()[0]]

def connct(db,DBNAME):
    global DB_EXC
    dbDir = '%s_%s' % (db,DBNAME)

    if db == 'sqlite':
        try:
            import sqlite3
        except ImportError as importError:
            try:
                from sqlite3 import dbapi2 as sqlite3
            except ImportError as importError:
                return None

        DB_EXC = sqlite3
        if not os.path.isdir(dbDir):
            os.mkdir(dbDir)
        cxn = sqlite3.connect(os.path.join(dbDir,DBNAME))

    elif db == 'mysql':
        try:
            import MySQLdb
            import __mysql_exception as DB_EXC

            try:
                cxn = MySQLdb.connect(db=DBNAME)
            except DB_EXC.OperationalError as operationErrors:
                print(operationErrors)
                try:
                    cxn = MySQLdb.connect(user = DBUSER)
                    cxn.query('crealte database %s' % DBNAME)
                    cxn.commit()
                    cxn.close()
                    cxn = MySQLdb.connect(db=DBNAME)
                except DB_EXC.OperationalError as operationErrors:
                    return None
        except ImportError as importErros:
            try:
                import mysql.connector
                import mysql.connector.erros as BD_EXC
                try:
                    cxn = mysql.connector.Connect(**{
                        'database': DBNAME,
                        'user': DBUSER,
                    })
                except DB_EXC.InterfaceError as interfaceErrors:
                    return None
            except ImportError as importErrors:
                return None
    else:
        return None

    return cxn

def create(cur):
    try:
        cur.execute('''
            create table users (
              login varchar(%d),
              userid INTEGER,
              projectid INTEGER 
            )
        ''' % NAMELEN)
    except DB_EXC.OperationalError as operationalErrors:
        drop(cur)
        create(cur)

def randName():
    pick = set(NAMES)
    while pick:
        yield pick.pop()

def insert(cur,db):
    if db == 'sqlite':
        cur.executemany('insert into users VALUES (?,?,?)' % [(who,uid,rand(1,5) for who,uid in randName())])
    elif db == 'mysql':
        cur.executemany('insert into users VALUES (%s,%s,%s)' % [(who,uid,rand(1,5) for who, uid in randName())])

def update(cur):
    fr = rand(1,5)
    to = rand(1,5)
    cur.execute('update users set projectid = %d' % (to,fr))
    return fr,to,getRC()

def delete(cur):
    rm = rand(1,5)
    cur.execute('delete from users where projectid = %d' % rm)
    return rm,getRC()

def dbDump(cur):
    cur.execute('select * from users')
    printf('\n%s' % ''.join(map(cformat,FIELDS)))
    for data in cur.fetchall():
        printf(''.join(map(tformat,data)))

def main():
    db = setup()
    printf('******Connecto to %r database*********' % db)
    cxn = connct(db)
    if not cxn:
        printf('ERROR : %r not supported or unreachable, exit ' % db)
    cur = cxn.cursor()

    printf('\n*******creating users table********')
    create(cur)

    printf('\n*********Inserting names into table*************')
    insert(cur,db)
    dbDump(cur)

    printf('\n*********Randomly moving folks****************')
    fr,to,num = update(cur)
    printf('\t(%d users moved) from (%d) to(%d)' % (num,fr,to))

    printf('\n*********Randomly choosing group***********')
    rm, num = delete(cur)
    printf('\t(group #%d; %d users removed' % (rm,num))
    dbDump(cur)

    printf('\n********Dropping users table*************')
    drop(cur)
    print('\n********Close cxns**********')
    cur.close()
    cxn.commit()
    cxn.close()


if __name__ == '__main__':
    main()
    pass 
    
    