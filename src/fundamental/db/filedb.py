#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

import shelve

if __name__ == "__main__":
    db = shelve.open('mdb')

    #db['xishi'] = 'xishihuansha'
    #db['diaochan'] = 'diaochabaiyue'
    #db['昭君'] = '昭君出塞'
    db['dcy'] = ['dcy','15093077823','shanghai','mywolr',4000]
    db['ltt'] = ['ltt','15093077824','tianjing','mywolr',2500]
    db['mxl'] = ['mxl','15093077825','beijing','mywolr',2000]

    '''
    print('-------anythin in operation-------------')

    for k,v in db.iteritems():
        print(k,v)

        if db.has_key('西施'):
            print('---------delete the xishi------')
        print('----the xishi have been deleted--------')

    for k,v in db.iteritems():
        print(k,v)
    '''

    for x in db.items():
        print(x[0])

    db.close()