#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = '330mlcc'

import collections
from random import choice

#使用collections.namedtuple构建简单的类表示纸牌.namedtuple用于构建只有少数属性而没有方法的对象
Card = collections.namedtuple('Card',['rank','suit'])

#用于实现点数判断扑克牌的大小
suit_values = dict(spades=3,hearts=2,diamonds=1,clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    # print(ranks)
    suits = 'spades diamonds clubs hearts'.split()
    # print(suits)

    def __init__(self):
        self.cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self.cards)

    #getitem把操作交给了self.cards列表，因此deck类自动支持切片
    def __getitem__(self, position):
        return self.cards[position]



if __name__ == '__main__':
    # beer_card = Card('7','diamonds')
    # print(beer_card)

    # deck = FrenchDeck()
    # for j in deck:
    #     print(j)
    # print('FrenchDeck中有多少张牌：',len(deck))
    #
    #取出第一张牌和最后一张牌
    # print(‘第一张牌：’deck[0])
    # print(‘最后一张牌：’deck[-1])

    # 随机抽取一张纸牌，使用random.choice
    # print(choice(deck))

    # 取出最上面的三张牌
    # print('最上面的三张牌：',deck[:3])
    # 先抽出第12张牌，然后每隔13章牌拿一张
    # print('先抽出第12张牌，然后每隔13章牌拿一张：',deck[12::13])

    #仅仅实现了__getitem__,一摞牌九可以实现迭代和反迭代
    # for card in deck:
    #     print('一摞牌实现迭代',card)
    #
    # for card in reversed(deck):
    #     print('一摞牌实现反迭代',card)

    #对扑克牌进行排序
    for card in sorted(deck,key=spades_high):
        print(card)

    pass

