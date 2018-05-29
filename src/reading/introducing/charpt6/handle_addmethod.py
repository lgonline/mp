#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: lgonline 
@license: Apache Licence  
@contact: lgonline@hotmail.com 
@site:  
@software: PyCharm 
@file: handle_addmethod.py 
@time: 11/7/17 10:33 PM 
"""


class myclass():
    def __init__(self,username):
        self.hidden_name = username

    def setUsername(self,username):
        print 'my name is setUsername'
        self.hidden_name = username

    def getUsername(self):
        print 'my name is getUsername'
        print self.hidden_name

    name = property(getUsername,setUsername)


class Circle():
    def __init__(self,radius):
        self.ra

if __name__ == "__main__":
    fowl = myclass('fowl')
    fowl.name

    fowl.name = 'abc'
    fowl.name

    #main()
    pass  