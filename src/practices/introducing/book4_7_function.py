#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = '330mlcc'

def menu(wine,entree,dessert):
    print {'wine':wine,'entree':entree,'dessert':dessert}

def buggy(arg,result=[]):
    result.append(arg)
    print result

if __name__ == '__main__':
    print "menu('chardonnay','chicken','cake')"
    menu('chardonnay','chicken','cake')

    print "menu('dunkelfelder','duck','doughnut')"
    menu('dunkelfelder', 'duck', 'doughnut')

    print '------------------------'
    buggy('b')
    pass

