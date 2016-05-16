#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'Administrator'

import textwrap

str = '''
Many managers and business owners understand the value of hiring a diverse group of employees,
but aren't quite sure of the steps that need to be taken towards reaching their goal of an inclusive and diverse workforce.
'''

print(textwrap.fill(str,width=50))

print("去除缩进")
print(textwrap.dedent(str))

print("结合fill和dedent")
#str = textwrap.dedent(str).strip()

for width in [45]:
    #输出了指定的宽度
    print(textwrap.fill(str,width=width))

if __name__ == "__name__":
    pass