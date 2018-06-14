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
@file: useList.py
@time: 18-6-7 下午10:50 
Description: 
"""


def main():
    empty_list = [] # 一个空的列表
    weekdays = ['Monday','Tuseday','Wednesday','Thursday','Friday']
    str = 'cat'
    print('将字符串转为列表：',list(str))
    print(weekdays)
    a_tuple = ('ready','fire','aim')
    print('将一个元组转换成列表：',list(a_tuple))
    print(list(a_tuple)[0])
    print('----------demo：一个包含列表的列表----------')
    small_birds = ['hummingbird','finch']
    extinct_birds = ['ddo','passenger pigeon','Norwegian Blue']
    carol_birds = [3,'French hens',2,'turtledoves']
    all_birds = [small_birds,extinct_birds,'macaw',carol_birds]
    print(all_birds)
    for all_bird in all_birds:
        print(all_bird)

    weekdays[0] = 'Mondays'
    print('使用offset修改元素(weekdays[0] = \'Mondays\'',weekdays)
    print('使用切片提取元素weekdays[::4] is ',weekdays[2::1])
    weekdays.append('Satusday')
    print('使用append，添加元素：',weekdays)
    small_birds.extend(extinct_birds)
    small_birds.extend(carol_birds)
    print('使用extends合并列表',small_birds)
    weekdays.insert(6,'Sunday')
    print('使用insert将元素插入指定位置：',weekdays)
    print('使用index查询特定值位置的元素:',weekdays.index('Sunday'))
    print('使用in判断值是否存在：','Sunday'in weekdays)
    print('使用count计算特定值出现的次数：',weekdays.count('Sunday'))
    print('使用join转换成字符串：',','.join(weekdays))
    weekdays.sort(reverse=True)
    print('使用sort对list进行排序：',weekdays)
    print('使用Len获取长度：',len(weekdays))
    pass


if __name__ == '__main__':
    main()
    pass 
    
    