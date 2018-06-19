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
@file: handleFileAndFolder.py
@time: 18-6-19 下午9:40 
Description: 
"""

import os,re

def main():
    print('当前python脚本的目录及路径,os.getcwd() : ',os.getcwd())
    print('返回指定目录下所有文件及目录名，os.listdir() : ',os.listdir())
    print('分离一个路径和文件os.path.split() : ',os.path.split(os.path.abspath(__file__)),type(os.path.split(os.path.abspath(__file__))))
    print('获取文件路径名,os.path.dirname() ： ',os.path.dirname(os.path.abspath(__file__)))
    print('获取文件名,os.path.basename() ： ', os.path.basename(os.path.abspath(__file__)))
    # print('读取环境变量os.getenv() : ',os.getenv())
    print('获取操作系统平台信息os.name : ',os.name)
    print('获取文件属性,os.stat() : ',os.stat(os.path.abspath(__file__)))
    # print(type(os.stat(os.path.abspath(__file__))))
    file_stat = str(os.stat(os.path.abspath(__file__)))
    #
    # for contents in file_stat:
    #     print(contents[0])
    # content = re.match(r'=(.*),',file_stat)
    contents = file_stat.split(',')
    # print(contents)
    # print(contents[2])
    for content in contents:
        results = content.split('=')
        print(results)
    pass


if __name__ == '__main__':
    main()
    pass 
    
    