#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

class Fruit:
    def __init__(self,*args):
        for arg in args:
            arg(self)

    def config(self,*args):
        for arg in args:
            arg(self)

    def hasHarvest(self):
        self.hasHarvest = True

    def hasNotHarvest(self):
        self.hasHarvest = False

    def setColor(color):
       def method(self):
           self.color = color
           return method

    def canEat(self):
        self.eat = True

    def canNotEat(self):
        self.eat = False