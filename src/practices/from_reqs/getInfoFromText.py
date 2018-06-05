#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = '330mlcc'

"""
从剪贴板获取文本，找出所有的电话号码和email并粘贴到粘贴板
"""

import re,pyperclip

if __name__ == '__main__':
    #电话号码正则匹配表达式
    phoneReget = re.compile(r'''
        (\d{3}|\(\d{3}\))?                      #area code
        (\s|-|\.)?                              #separator
        (\d{3})                                 #first 3 digits
        (\s|-|\.)                               #separator
        (\d{4})                                 #last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))           #extension
    ''',re.VERBOSE)

    #email正则匹配表达式
    emailRegex = re.compile(r'''
        [a-zA-Z0-9._%+-]+                       #username
        @                                       #@symbol
        [a-zA-Z0-9.-]+                          #DOMAIN NAME
        (\.[a-zA-Z]{2,4})                       #dot-something
    ''',re.VERBOSE)

    #在粘贴板中找到所有匹配
    text = str(pyperclip.paste())
    matches = []
    for groups in phoneReget.findall(text):
        phoneNum = '-'.join([groups[1],groups[3],groups[5]])
        if groups[8] != '':
            phoneNum += ' x'+groups[8]
        matches.append(phoneNum)

    for groups in emailRegex.findall(text):
        matches.append(groups[0])

    #所有匹配连成一个字符串，复制到剪贴板
    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print 'Copied to clipboard:'
        print '\n'.join(matches)
    else:
        print 'No phone numbers or email addresses found.'
