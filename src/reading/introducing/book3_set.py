#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = '330mlcc'

#使用in测试值是否存在
drinks = {
    'martini':{'vodka','vermouth'},
    'black russian':{'vodka','kahlua'},
    'whie russian':{'cream','kahlua','vodka'},
    'manhattan':{'rye','vermouth','bitters'},
    'screwdriver':{'orange juice','vodka'}
    }

def search_content():
    print 'in判断是否在集合中。demo1'
    for name,content in drinks.items():
        if 'vodka' in content:
            print name
    print 'in判断是否在集合中。demo2'
    for name,content in drinks.items():
        if 'vodka' in content and not('vermouth' in content or 'cream' in content):
            print name
    print '判断含有果汁或苦艾酒'
    for name,content in drinks.items():
        if content & {'vermouth','orange juice'}:
            print name
    print '想要伏特加但不需要乳脂也不需要苦艾酒'
    for name,content in drinks.items():
        if 'vodka' in content and not content & {'vermouth','orange juice'}:
            print name

    print '合并运算符号...'
    bruss = drinks['black russian']
    wruss = drinks['whie russian']
    a = {1,2}
    b = {2,3}
    #使用&或intersection()获得交集；使用|或union()获得并集；
    # 使用-或difference()获得差集，即第一个集合出现但第二个集合不出现；使用^或symmetric_difference()获得异或集，即两个集合中出现一次
    #使用<=或issubset()判断一个集合是否是另一个集合的子集，第一个集合的所有元素都出现在第二个集合中
    #使用>=或issuperset()判断超集，即第二个集合的所有元素都出现在第一个集合中
    print 'bruss & wruss is : ',bruss & wruss
    print 'a | b is : ',a|b

if __name__ == '__main__':
    search_content()

