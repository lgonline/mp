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
@file: load_json_without_dupes.py
@time: 18-6-12 下午11:46 
Description: 
"""

ordered_pairs = {'1':'111','2':'222','3':'333'}

def main(ordered_pairs):
    my_dict = dict()
    for key,value in ordered_pairs:
        if key in my_dict:
            raise ValueError("Duplicate key:{}".format(key,))
        else:
            my_dict[key] = values

    return my_dict
    pass


if __name__ == '__main__':
    main()
    pass 
    
    