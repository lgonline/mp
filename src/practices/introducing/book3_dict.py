#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = '330mlcc'

bierce = {
    'day':'A period of twenty-four hours, mostly misspent',
    'positive':'Mistaken at the top of one\'s voice',
    'misfortune':'The kind of fortune that never misses',
}

print 'print the dict : ',bierce

#使用dict()将列表转换为字典
lists = [['a','a'],['b','b'],['c','c']]
dicts = dict(lists)
print dicts

#使用key添加或修改元素
chinese = {'gang':'liu','ethan':'lee','gary':'liu'}
print 'Before person : ',chinese
chinese['gary'] = 'lee'
print 'After person : ',chinese

#使用update合并字典
japanese = {'toyoto':'auto'}
print japanese
chinese.update(japanese)
print 'person is : ', chinese

#使用del删除指定键的元素，clear删除所有元素，in判断是否存在，keys获取所有键,values获取所有值，items获取所有键值
print chinese.keys()
print chinese.values()
print chinese.items()

