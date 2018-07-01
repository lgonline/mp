#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = '330mlcc'

from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib.request import urlopen as urlopen

REGEX = compile('#([\d.]+) in Books.')
AMZN = 'http://amazon.com/dp/'
ISBNs = {
    '0132269937':'Core Python Programming',
    '0132356139':'Python Web Development with Django',
    '0137143419':'Python Fundamentals',
}

def getRanking(isbn):
    page = urlopen('%s%s' % (AMZN,isbn))
    data = page.read()
    page.close()
    return REGEX.findall(data)[0]

def _showRanking(isbn):
    print('- ',(ISBNs[isbn]),' ranked ',getRanking(isbn))

def main():
    print('At ',ctime(),' on Amazon...')
    for isbn in ISBNs:
        _showRanking(isbn)

@register
def _atexit():
    print('All done at : ',ctime())


if __name__ == '__main__':
    main()
    pass

