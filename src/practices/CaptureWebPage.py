#!/usr/bin/python
#-*- coding: utf-8 -*-

'''
目标：抓取oschina上面的代码分享python块区下的 标题和对应URL
'''

#from lxml import

__author__ = 'liugang5'

class Capture_OSChina:
    def __init__(self):
        print('the programing is beginning.')

    def get_html_object(self,url = 'http://www.oschina.net/code/list?lang=python&catalog=&show=time&sort=&p=1'):    #传入地址，返回一个xpath对象
        set_http_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'}
        #obj = etree.HTML(requests.get(url,headers = tou).content)    # 实例化可以被lxml操作的对像
        #return obj):

if __name__ == "__main__":
    pass