#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: 330mlcc 
@license: Apache Licence  
@contact: lg_online@126.com 
@site:  
@software: PyCharm 
@file: maiin
@time: 18-6-4 下午11:37 
Description: 
"""

import sys
# reload(sys)from ..checkip.ipip import IP
# sys.setdefaultencoding("utf-8")

import os

from src.practices.checkip.ipip import IP
from src.practices.checkip.ipip import IPX

IP.load(os.path.abspath("mydata4vipday2.dat"))
print(IP.find("118.28.8.8"))

IPX.load(os.path.abspath("mydata4vipday2.datx"))
print(IPX.find("118.28.8.8"))
    