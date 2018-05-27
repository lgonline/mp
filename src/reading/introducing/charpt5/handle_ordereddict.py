#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: lgonline 
@license: Apache Licence  
@contact: lgonline@hotmail.com 
@site:  
@software: PyCharm 
@file: handle_ordereddict.py 
@time: 11/3/17 11:07 PM 
"""


from collections import OrderedDict

def func():
    quotes = OrderedDict([('Moe','Awise guy, huy?'),
                          ('Larry','Ow!'),
                          ('Curly','Nyuk nyuk')])

    for stooge in quotes:
        print stooge
    pass


class main():
    func()
    def __init__(self):
        pass


if __name__ == "__main__":
    main()
    pass  