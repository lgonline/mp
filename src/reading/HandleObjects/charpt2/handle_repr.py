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
Description: 不可变对象和继承的默认行为♠♥♦♣
"""

class Card:
    insure = False

    def __init__(self,rank,suit,hard,soft):
        self.rank = rank
        self.suit = suit
        self.hard = hard
        self.soft = soft

    def __repr__(self):
        return "{__class__.__name__}(suit={suit!r},rank={rank!r}".format(__class__=self.__class__,**self.__dict__)

    def __str__(self):
        return "{rank}{suit}".format(**self.__dict__)

class NumberCard(Card):
    def _points(self,rank,suit):
        super().__init__(str(rank),suit,rank,rank)

class AceCard(Card):
    def __init__(self,rank,suit):
        super().__init__("A",suit,1,11)

class FaceCard(Card):
    def __init__(self,rank,suit):
        super().__init__({11:'J',12:'Q',13:'K'}[rank],suit,10,10)


if __name__ == '__main__':
    c1 = AceCard(1,'♥')
    print(c1)
    pass
    