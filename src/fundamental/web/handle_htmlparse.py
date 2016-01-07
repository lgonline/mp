#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

from urllib.parse import unquote,unquote_plus,urlparse
import html.parser as htmlparseor
import urllib.request,urllib.response
import re
import os

urlContent = []
mycontent = []

class HtmlParsor(htmlparseor.HTMLParser):
    mflag = False
    def handle_starttag(self,tag,attrs):
        print('starting a tag : ',tag)
        print()

        if str(tag).startswith("title"):
            print(tag)
            self.mflag = True
            for attr in attrs:
                print(" The attribute is : ",attr)

    def handle_endtag(self,tag):
        if tag == "title":
            self.mflag = False
            print("close a attribute : ",tag)

    def handle_data(self,data):
        if self.mflag == True:
            print("The data is : ",data)


class SelfHtmlParser():
    def __init__(self):
        htmlparseor.HTMLParser.__init__(self)
        #self.value = value


    def __getattr__(self, item):
        print(item)
        regx = re.compile(r'<'+item+r'.*?>.*</'+item+r'>')
        return re.findall(regx,self)

    '''
    def handle_startendtag(self, tag, attrs):
        #redefine the tag to handle the starttag tag
        if tag == 'a':
            for name,value in attrs:
                if name == 'href':
                    print(value)

    def handle_data(self, data):
        if data != '':
            urlContent.append(data)
    '''

if __name__ == "__main__":
    #demo for
    '''
    url = 'https://www.baidu.com/s?wd=pycharm%20web%20tomcat%20%E9%83%A8%E7%BD%B2&rsv_spt=1&rsv_iqid=0xb25600d300005801&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&oq=pycharm%20tomcat%20%E9%83%A8%E7%BD%B2&rsv_t=02279cxCOeMjpOzNhCqHcXCv7p2JPX29wSb37PHvoVdhnh1%2FPejpS3fVk84ZcHCYz79c&inputT=595&rsv_pq=966a0ca000007720&rsv_sug3=27&rsv_sug1=7&rsv_sug2=0&rsv_sug7=100&rsv_sug4=1986&rsv_sug=1'
    unquoteurl = unquote(url)
    urlparses = urlparse(unquoteurl)
    print(unquoteurl)

    #print urlparse information
    for info in urlparses:
        print(info)
    '''

    #demo for htmlparser
    '''
    myhtmlparser1 = HtmlParsor()
    myhtmlparser1.feed("<html><title>hello</title><body>hello world!!!</body></html>")
    myhtmlparser1.close()
    '''

    #get url's content
    #myrequest = urllib.request('http://www.4hb.com/letters/ltrdelacct4.html')
    file = "D:\\INFOR.html"

    shp = SelfHtmlParser()
    response = urllib.request.urlopen('http://www.4hb.com/letters/ltrdelacct4.html')
    mycontent = response.read()
    reg = shp(mycontent)
    openfile = open(file,"a+")
    response.close()
    print(reg.title)

    pass