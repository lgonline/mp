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
@file: initInSubClass.py
@time: 18-6-13 下午7:46 
Description: 在子类中实现init方法
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

class AceCard(Card):
    insure = True
    def _points(self):
        return 1,11

class FaceCard(Card):
    def _points(self):
        return 10,10

d1 = [AceCard('A', '♠'), NumberCard('2', '♠'), NumberCard('3', '♠'), ]

#为所有卡片的花色单独创建一个类
class Suit:
    def __init__(self,name,symbol):
        self.name = name
        self.symbol = symbol

    def __repr__(self):
        return self.symbol
        pass

Club, Diamond, Heart, Spade = Suit('club', '♣'), Suit('club', '♦'), Suit('club', '♥'), Suit('club', '♠')

class CardFactory:
    def rank(self,rank):
        self.class_,self.rank_str={
            1: (AceCard, 'A'),
            11: (FaceCard, 'J'),
            12: (FaceCard, 'Q'),
            13: (FaceCard, 'K'),
        }.get(rank, (NumberCard, str(rank)))

        return self

    def suit(self, suit):
        return self.class_(self.rank_str, suit)



# print(type(d1))

d2 = [AceCard('A', Spade), NumberCard('2', Spade), NumberCard('3', Spade), ]

def card(rank,suit):
    if rank == 1: return AceCard('A',suit)
    elif 2 <= rank < 11: return NumberCard(str(rank),suit)
    elif 11<= rank < 14:
        name = {11:'J',12:'Q',13:'K'}[rank]
        return FaceCard(name,suit)
    else:
       raise Exception('Rank out of rank')

deck = [card(rank,suit) for rank in range(1,14) for suit in (Club,Diamond,Heart,Spade)]

print(deck)

    #
    # for d in deck:
    #     print(d)
    #
    #
    # cards = Card()
    # Club,Diamond,Heart,Spade = Suit('club','♣'),Suit('club','♦'),Suit('club','♥'),Suit('club','♠')
    # cards = [AceCard('A',Spade),FaceCard('3',Spade),NumberCard('2',Spade),]
    # print(cards)
    # print('hello')
# pass
    
    