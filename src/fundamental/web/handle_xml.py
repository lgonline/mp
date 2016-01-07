#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

import xml.sax

class HandleXML(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ''
        self.type = ''
        self.format = ''
        self.year = ''
        self.rating = ''
        self.stars = ''
        self.description = ''

    #handle start event
    def startDocument(self,tag,attrs):
        print('--------start--------')
        self.CurrentData = tag
        if tag == 'movie':
            print('-----Movie-------')
            title = attrs['title']
            print("Title : ",title)

    #handle end event
    def endDocument(self,tag):
        print('-----------end---------')
        if self.CurrentData =='type':
            print("Type : ",self.type)
        elif self.CurrentData =='format':
            print("Format : ",self.format)
        elif self.CurrentData =='year':
            print("Year : ",self.year)
        elif self.CurrentData =='rating':
            print("Rating : ",self.rating)
        elif self.CurrentData =='stars':
            print("Stars : ",self.stars)
        elif self.CurrentData =='description':
            print("Description : ",self.description)
        self.CurrentData = ''

    #handle content event
    def characters(self, content):
        if self.CurrentData =='type':
            print("Type : ",self.type)
        elif self.CurrentData =='format':
            print("Format : ",self.format)
        elif self.CurrentData =='year':
            print("Year : ",self.year)
        elif self.CurrentData =='rating':
            print("Rating : ",self.rating)
        elif self.CurrentData =='stars':
            print("Stars : ",self.stars)
        elif self.CurrentData =='description':
            print("Description : ",self.description)

if __name__ == "__main__":
    #start a xmlreader
    myparser = xml.sax.make_parser()

    #turn off namepasaces
    myparser.setContentHandler

    #re-writer contexthandler
    Handler = HandleXML()
    myparser.setContentHandler(Handler)
    myparser.parse('infor.xml')
    pass