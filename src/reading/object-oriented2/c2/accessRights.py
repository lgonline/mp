#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
@author: mlcc
@file: accessRights.py
@time: 19-5-1 下午6:03 
Description: 
"""

class SecretString:
    def __init__(self,plain_string,pass_phrase):
        self.__plain_string = plain_string
        self.__pass_phrase = pass_phrase

    def decrypt(self,pass_phrase):
        if pass_phrase == self.__pass_phrase:
            return self.__plain_string

        else:
            return 'No pass phrase'

if __name__ == '__main__':
    s1 = SecretString("liugang52","abcd1234")
    print("s1.decrypt('abcd1234') is ",s1.decrypt("abcd1234"))
    print("s1.decrypt('') is ",s1.decrypt(""))
    pass