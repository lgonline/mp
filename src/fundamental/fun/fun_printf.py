#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

#import sys

#def myprintf(file,fmt,*args):
#    print(sys.stdout,fmt, *args)

def make_table(data,**parms):
    fgcolor = parms.pop("fgcolor","black")
    bgcolor = parms.pop("bgcolor","white")
    width = parms.pop("width",None)

    if parms:
        raise TypeError("Unsupported configuration option %s ", list(parms))

    for datas in data:
        print("fgcolor is ",fgcolor,"bgcolor is ",bgcolor," and width is ",width)

if __name__ == "__main__":
#    myprintf(2,'hello',3.45)
    data = [1,2,3]
    make_table(data,fgcolor="red",bgcolor="white",width=400)