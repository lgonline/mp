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
@file: dictComprehension.py
@time: 18-8-30 下午10:54 
Description:
字典T
"""

import sys
import re
import collections

def handleDictComprehension():
    '''
    字典推导式的例子
    :return:
    '''
    DIAL_CODES = [
        (86, 'china'),
        (91, 'India'),
        (1, 'United States'),
        (62, 'Indonesia'),
        (55, 'Brazil'),
        (92, 'Pakistan'),
        (880, 'Bangladesh'),
        (234, 'Nigeria'),
        (7, 'Russia'),
        (81, 'Japan'),
    ]

    country_code = {country: code for code, country in DIAL_CODES}
    print(country_code)

    results = {code: str(country).upper() for country, code in DIAL_CODES}
    print(results)

    print('DIAL_CODES.__iter__() is : ',DIAL_CODES.__iter__())

    pass

def countWordInFileUseSetdefault():
    """
    使用setdefault处理找不到的键
    :return:
    """
    WORD_CONTENT = re.compile(r'\w+')
    index = {}

    with open(sys.argv[1],encoding='utf-8') as fp:
        for line_no, line in enumerate(fp,1):
            # print(line_no," : ",line)
            for match in WORD_CONTENT.finditer(line):
                word = match.group()
                # print('word is : ',word)
                column_no = match.start() + 1
                # print('column_no is : ',column_no)
                location = (line_no,column_no)

                # 以下这是一种非常不好的实现
                # 提取word出现的情况，如果没有记录就返回空
                # occurrences = index.get(word,[])
                # 把单词新出现的位置添加到列表后面
                # occurrences.append(location)
                # 把新的列表放回到字典种，多了一次查询操作
                # index[word] = occurrences

                # 建议使用好的方法替换以上的逻辑
                # 如果单词不存在，把单词和空列表放进映射，然后返回这个空列表，可以不进行二次查找就可更新列表
                index.setdefault(word,[]).append(location)

    for word in sorted(index,key=str.upper):
        # sorted函数的key=参数没有调用Str.upper《而是把这个方法的引用传递给Sorted函数，排序时，单词被规范成统一格式
        print(word,index[word])

def countWordInFileUseDefaultdict():
    WORD_CONTENT = re.compile(r'\w+')
    # 把List构造方法作为Default_factory来创建一个Defaultdict
    index = collections.defaultdict(list)

    with open(sys.argv[1], encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for match in WORD_CONTENT.finditer(line):
                word = match.group()
                # print('word is : ',word)
                column_no = match.start() + 1
                # print('column_no is : ',column_no)
                location = (line_no, column_no)
                # 如果index没有word的记录，那么default_Factory会被调用
                index[word].append(location)

    for word in sorted(index, key=str.upper):
        print(word, index[word])

def main():
    # handleDictComprehension()
    countWordInFileUseSetdefault()

if __name__ == '__main__':
    main()
    pass
