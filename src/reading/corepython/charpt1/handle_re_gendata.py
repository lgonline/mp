#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: 330mlcc 
@license: Apache Licence  
@contact: lg_online@126.com 
@site:  
@software: PyCharm 
@file: handle_re_gendata
@time: 18-5-14 下午11:55 
Description: 
"""

from random import randrange,choice
from string import ascii_letters as lc
from sys import maxsize
from time import ctime

basic_data = ('com','edu','net','org','gov') #随机生成的email地址中选取一个

if __name__ == '__main__':
    # for i in range(randrange(6,8)):
    #     dtint = randrange(maxsize)          #生成一个32位整数
    #     print(dtint) # for i in range(randrange(6,8)):
    #     dtint = randrange(maxsize)          #生成一个32位整数
    #     print(dtint)
    #     dtstr = ctime(dtint)                #将生成的整数转换为时间（19700101至今）
    #     llen = randrange(4,8)               #生成电子邮件地址，4-7个字符
    #     login = ''.join(choice(lc) for j in range(llen))    #lc的作用为转换为小写
    #     dlen = randrange(llen,13)           #
    #     dom = ''.join(choice(lc) for j in range(dlen))
    #     print('%s::%s@%s::%d-%d-%d' % (dtstr,login,dom,choice(basic_data),dtint,llen,dlen))

    for i in range(randrange(9,15)):
        dtint = randrange(maxsize)          #生成一个32位整数
        print(dtint)
    pass 
    
    