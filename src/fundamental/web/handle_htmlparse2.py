#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

import html.parser as parser
import os

#global var
HTML_FILE = ''
HTML_STR = ''

class MyHTMLParser(parser.HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Meet starttag:{} start handle:{}".format(tag,tag))

    def handle_endtag(self, tag):
        print("Meet endtag:{} start handle:{}".format(tag,tag))

    def handle_data(self, data):
        print("Meet data:{} start handle:{}".format(data,data))

    def handle_comment(self, data):
        print("Meet comment:{} start handle:{}".format(data,data))

    def handle_decl(self, decl):
        print("Meet declaration:{} start handle:{}".format(data,data))

def parser_test(html_str):
    #parser html source file
    parser = MyHTMLParser(strict = False)
    parser.feed(html_str)
    parser.close()

def read_html_file(path):
    #read the information from html file
    content = ''
    if os.path.exists(path):
        print('start read file:[{}]'.format(path))
        with open(path,'r') as pf:
            for line in pf:
                content += line
            pf.close()
            return content
    else:
        print('the path[{}] doesn\'t exist!'.format(path))
        return content

def init():
    #source file path
    global HTML_FILE
    HTML_FILE = 'D:\\INFO.html'
    global HTML_STR
    HTML_STR = read_html_file(HTML_FILE)

def main():
    init()
    print('source html\n{}'.format(HTML_STR))
    print('*'*50)
    parser_test(HTML_STR)


if __name__ == "__main__":
    main()
    pass