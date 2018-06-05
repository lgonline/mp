#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = '330mlcc'

if __name__ == '__main__':
    myName = []
    result = []

    while True:
        print "Enter the name for you "+str(len(myName)+1)+'(Or enter nothing to stop.):'
        yourname = raw_input()
        if yourname == '':
            break

        myName.append(yourname)

    '''
    print 'The name are : '
    print myName
    for aaa in myName:
        print '\t'+aaa


    if "www" in myName:
        print "the www in myname"
    else:
        print "the www not in myname"
    '''

    for i in range(len(myName)):
        print i
        result = int(myName[i])
        print result

    pass

