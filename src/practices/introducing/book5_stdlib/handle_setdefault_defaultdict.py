#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = '330mlcc'

from collections import defaultdict

#读取字典不存在的键值会出现异常，setdeafult在键值不存在是添加一项
def handle_setdefault():
    periodict_table = {'hydrogen':1,'Helium':2}

    print 'periodict最初的key和values : ',periodict_table
    print ''
    carbon = periodict_table.setdefault('carbon',3)

    #print carbon

    print 'carbon之前不再periodict_table中，现在已经被默认添加了 : ',periodict_table
    print ''

    #把一个不同的默认值付给已经存在的键，不会改变原来的值
    helium = periodict_table.setdefault('helium',947)
    print 'helium被新赋了一只值947，但没有改变dict中的值 : ', periodict_table

#defaultdict创建字典时对每个新的键都制定默认的值，参数是一个函数
def handle_defaultdict():
    def no_idea():
        return 'Hub?'

    bestiary = defaultdict(no_idea)
    bestiary['A'] = 'Abominable Snowman'
    bestiary['B'] = 'Basilisk'

    print 'bestiary A is : ', bestiary['A']
    print 'bestiary B is : ', bestiary['B']
    print 'bestiary C is : ', bestiary['C']

    #int是一种定义计数器的方式
    food_counter = defaultdict(int)
    for food in ['spam','spam','spam','eggs']:
        food_counter[food] += 1

    for food,count in food_counter.items():
        print 'the food of ',food,' and the count is : ',count


if __name__ == '__main__':
    print '********************call hadle_setdefault() as follows : ***********************'
    handle_setdefault()

    print '********************call handle_defaultdict() as follows : ***********************'
    handle_defaultdict()
    pass

