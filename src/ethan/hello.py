#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = '330mlcc'

import sys

if __name__ == '__main__':
    #print 'Peter, how are you?'

    #print '-----------------------'

    k=5
    l=0

    #for i in range(1,5):
    #    for j in range(1,5):
    #        sys.stdout.write('*')
    #    print ''

    #print '=================================='

    '''
    for i in range(1,10):
        for i in range(1,5):
            for j in range(l+i):
                sys.stdout.write('*')
            print ''
        #print '=================================='

        for i in range(1,5):
            for j in range(k-i):
                sys.stdout.write('*')
            print ''
    '''


    for i in range(1, 5):
        for j in range(l + i):
            sys.stdout.write('*')
        print ''
        # print '=================================='

    for i in range(1, 5):
        for j in range(k - i):
                sys.stdout.write('*')
        print ''


    for ii in range(1,50):
        sys.stdout.write('=')
    pass