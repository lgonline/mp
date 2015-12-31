#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

x = 37

def call_fun(func):
    return func()

def helloworld():
    #print("Hello World!!!")
    return "Hello World!!! x is ",x

if __name__ == "__main__":
    call_fun(helloworld())