#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

class HTMLRenderer(Handler):
    '''

    '''
    def start_documnet(self):
        print('<html><head><title>...</title></head><body>')

    def end_document(self):
        print("</body></html>")

    def start_paragraph(self):
        print('<p>')

    def end_paragraph(self):
        print('</p>')

    def start_heading(self):
        print('<h2>')

    def end_heading(self):
        print('</h2>')

    def start_list(self):
        print('ul')

    def end_list(self):
        print('/ul')

    def start_listitem(self):
        print('<li>')

    def end_listitem(self):
        print('</li>')

    def start_title(self):
        print('<h1>')

    def end_title(self):
        print('</h1>')

if __name__ == "__main__":
    pass