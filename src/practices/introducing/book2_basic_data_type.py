#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = '330mlcc'

user = '真正的英雄'
#使用加号来拼接
a = '是谁'
print user+a


#使用星号复制
star = 'Na' * 4
print star

#使用[]提取字符
char = 'abcdefghigklmnopqrstuvwxyz'
print char[8]
#start:开始，end:结束，step: 每隔step个取一个
print '分片操作 : [start:end:step]' , char[8:16]
print '分片操作 : [start:end:step]' , char[8:24:2]

#使用split分割
splits = 'get gloves,get mask,give cat,get vitamin, call ambulance'
print 'the result when using split method is : ',splits.split(',')
print type(splits)

poem = '''All that doth folow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet'''

#字符串操作方法
#是否以all开头，
print '是否以ALL开头 : ',poem.startswith('All')
print '是否以ALL结尾 : ',poem.endswith('All')
print '单词is第一次出现的位置 : ',poem.find('is')
print '单词is最后一次出现的位置 : ',poem.rfind('is')
print 'is在字符串中出现了多少次 : ',poem.count('is')