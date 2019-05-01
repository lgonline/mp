#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
@version: 
@Software: mp
@author: mlcc
@file: initInBaseClass.py
@time: 19-4-4 下午9:16 
Description: 在基类中实现__init__()方法♠♥♦♣
"""

class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

        self.hard, self.soft = self.__points()

    def printCard(self):
        print(self.rank," , ",self.suit)

class NmuberCard(Card):
    def __points(self):
        return int(self.rank),int(self.rank)

class AceCard(Card):
    def __points(self):
        return 1,11

class FaceCard(Card):
    def __Card__points(self):
        return 10,10

if __name__ == '__main__':
    f = FaceCard("A","♠")
    f.printCard()
    pass