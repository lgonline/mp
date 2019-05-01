#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
@author: mlcc
@file: Notes.py
@time: 19-5-1 下午6:24 
Description: 
"""

import datetime

last_id = 0

class Note:
    def __init__(self,memo,tags = ''):
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self,filter):
        return filter in self.memo or filter in self.tags

#
# if __name__ == '__main__':
#     n1 = Notes("hello my notes",tags="python")
#     print(n1.id)
#     print(n1.creation_date)
#     print(n1.memo)
#     print(n1.tags)
#     pass