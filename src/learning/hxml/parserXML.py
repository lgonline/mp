#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

'''
ElementTree生来就是为了处理XML，它在Python标准库中有两种实现：一种是纯Python实现的，如xml.etree.ElementTree，另一种是速度快一点的xml.etree.cElementTree。注意：尽量使用C语言实现的那种，因为它速度更快，而且消耗的内存更少。
'''

import sys
import xml.sax

class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    #start to handle the element
    def startElement(self, tag, attrs):
        self.CurrentData = tag
        if tag == "movie":
            print("**********Movie**********")
            title = attrs['title']
            print("Title",title)

    #end to handle the element
    def endElement(self, tag):
        if self.CurrentData == "type":
            print("Type:",self.type)
        elif self.CurrentData == "format":
            print("Format:",self.format)
        elif self.CurrentData == "year":
            print("Year:",self.year)
        elif self.CurrentData == "rating":
            print("Rating:",self.rating)
        elif self.CurrentData == "stars":
            print("Stars:",self.stars)
        elif self.CurrentData == "description":
            print("Description:",self.description)
        self.CurrentData = ""

    #内容事件
    def characters(self,content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "format":
            self.format = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "rating":
            self.rating = content
        elif self.CurrentData == "stars":
            self.stars = content
        elif self.CurrentData == "description":
            self.description = content

if __name__ == "__main__":
    #创建一个xmlreader
    parser = xml.sax.make_parser()
    #trun off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 重写 ContextHandler
    Handler = MovieHandler()
    parser.setContentHandler(Handler)
    parser.parse('a.xml')