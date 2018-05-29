#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = '330mlcc'

#使用[]或()创建列表，使用list()将其它数据类型转换成list类型
mylists = ['aaa','bbb','ccc']
print 'mylists[2] is : ',mylists[2]

#包含列表的列表
samll_birds = ['hummingbird','finch']
extinct_birds = ['dodo','passenger pigeon','Norwegian Blue']
carol_birds = [3,'French hens',2,'turtledoves']
all_birds = [samll_birds,extinct_birds,'macaw',carol_birds]
print '包含列表的列表 : ',all_birds

#使用append将元素添加到尾部，使用extend或+=合并列表，使用inert在指定位置插入元素，使用del删除指定位置元素，使用remove删除指定元素
all_birds.append('china hens')
print '包含列表的列表 append(\'china hens','china bird\') : ',all_birds
japen_birds = ['toyoki hens','japen bird']
print '包含列表的列表 extend(japen_birds) : ',all_birds.extend(japen_birds)
print len(all_birds)

#使用insert,在指定位置插入元素
all_birds.insert(5,japen_birds)
print all_birds
print len(all_birds)

#使用index查询特定字符
print "使用index()在all_birds查询特定字符china hens : ",all_birds.index('china hens')

#使用in查询特定字符是否存在
print "使用in()在all_birds查询特定字符china : ", 'china hens' in all_birds

#使用count查询特定字符存在的次数
print "使用count在all_birds查询特定字符bird出现的次数 : ", all_birds.count('china hens')

#使用join将list转换为字符串
#print "使用join将list转换为字符串 : ", ','.join(all_birds)

#使用sort重新排序
print "使用sort重新排序 : ", all_birds.sort()

for str in all_birds:
    print str

