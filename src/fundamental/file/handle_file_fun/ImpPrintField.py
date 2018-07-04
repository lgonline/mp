__author__ = 'Administrator'

from datetime import datetime
import os

pwd = os.path.abspath('.')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))

print('************************************************************')
import os
def select(fileName,path = ''):
    _list = [x for x in (os.listdir('.') if path == '' else os.listdir(path))]
    for _file in _list:
        if os.path.isfile(os.path.join(path,_file)):
            if fileName in _file:
                print(_file)
        elif os.path.isdir(os.path.join(path,_file)):
            select(fileName,os.path.join(path,_file))

select('use')

print('==============================================================')
name = input('input name of finding file: ')
def findfile(name,path='.'):
    print('path : %s'%path)
    pwd = os.path.abspath(path)
    print(os.listdir(pwd))
    for f in os.listdir(pwd):
        if os.path.isdir(f):
            findfile(name,f)
        if os.path.isfile(f) and (name in os.path.split(f)[1]):
            print('The file in:',os.path.join(pwd,f))

findfile(name)