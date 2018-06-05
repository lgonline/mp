#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = '330mlcc'

from collections import Counter

def handle_counter():
    breakfast = ['spam','spam','eggs','soap']
    breakfast_counter = Counter(breakfast)
    print 'the breakfast is : ',breakfast_counter
    print ''
    lunchs = ['eggs','eggs','bacon']
    lunchs_counter = Counter(lunchs)
    print 'the lunch is : ',lunchs_counter
    print ''
    print '早餐和午餐的数量统计:',breakfast_counter+lunchs_counter
    print ''
    print '早餐和午餐的差异',breakfast_counter-lunchs_counter
    print ''
    print '午餐和早餐的差异',lunchs_counter-breakfast_counter
    print ''
    print '午餐和早餐的交集', lunchs_counter & breakfast_counter
    print ''
    print '午餐和早餐的并集', lunchs_counter | breakfast_counter

if __name__ == '__main__':
    print '********************call handle_counter method******************************'
    handle_counter()
    pass

