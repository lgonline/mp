# -*- coding: utf-8 -*-
# @Time    : 2018/6/1 17:09
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : main.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com

"""
https://github.com/17mon/python/blob/master/main.py
"""

# from imp import reload
import os
# reload(sys)
# from handle_ip import IP
from src.practices.ipinfo.handle_ip import IP
from src.practices.ipinfo.handle_ip import IPX

# sys.setdefaultencoding('ut-8')

IP.load(os.path.abspath('mydata4vipday2.dat'))
print(IP.find('118.28.8.8'))

IPX.load(os.path.abspath('mydata4vipday2.dat'))
print(IPX.find('8.8.8.8'))

