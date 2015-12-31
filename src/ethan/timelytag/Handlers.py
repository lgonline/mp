#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

'''
    一个处理程序的超类，负责产生标记文本，接受来自文本分析器的具体指令

    这个程序堪称是整个“项目”的基石所在：提供了标签的输出，以及字符串的替换。理解起来也比较简单。
'''

class Handler:
    #callback负责在给定一个前缀如sart_和一个名字如paragraph后查找正确的方法，如start_paragraph
    def callback(self,prefix,name,*args):
        #它使用以None作为默认值的getattr方法来完成工作，如果从getattr返回的对象能被调用，那么对象就可以用提供的任何额外的参数来调用
        #如对应的对象存在，那么调用handler.callback('start_','paragraph')就会调用不带参数的handle.start_paragraph
        method = getattr(self,prefix+name,None)
        if callable(method):
            return method(*args)

    def start(self,name):
        self.callback('start_',name)

    def end(self,name):
        self.callback('end_',name)

    #不直接调用callback，返回一个新函数，这个函数被当成re.sub中的替换函数来使用
    def sub(self,name):
        def substitution(match):
            result = self.callback('sub_',name,match)
            if result is None:
                match.group(0)
            return result
        return substitution


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

    def sub_emphasis(self,match):
        return '<em>$s</em>' % match.group(1)

    def sub_url(self,match):
        return '<a href="%s">%s</a>' % (match.group(1),match.group(1))

    def sub_mail(self,match):
        return '<a href="mail to:%s>%s</a>' % (match.group(1),match.group(1))

    def feed(self,data):
        print(data)

if __name__ == "__main__":
    pass