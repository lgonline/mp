#!/usr/bin/env python  
# -*- coding: utf-8 -*-

""" 
@version: v1.0 
@author: 330mlcc 
@Software: PyCharm
@license: Apache Licence  
@Email   : mlcc330@hotmail.com
@contact: 3323202070@qq.com
@site:  
@software: PyCharm 
@file: handle_repr.py
@time: 18-6-13 下午9:56 
Description: 
"""

class Card:
    insure = False

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        self.hard,self.soft = self._points()

    def __eq__(self, other):
        return self.suit == other.suit and \
            self.rank == other.rank and \
               self.hard == other.hard and self.soft == other.soft

    def __repr__(self):
        return "{__class__.__name__(suit={suit!r},rank={rank!r}".format(\
            __class__=self.__class__,**self.__dict__)

    def __str__(self):
        return "{rank}{suit}".format(**self.__dict__)

class NumberCard(Card):
    def _points(self):
        return int(self.rank),int(self.suit)

x = NumberCard('2','f')
# x = NumberCard('2','2')
print(str(x))
    