#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/14 17:21
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : xlsx_test.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com

"""

"""

import os,xlwt

# path = os.path.abspath(__file__)
# print(path)
# path1 = os.path.basename(os.path.abspath(__file__))
# print(path1)
path1 = os.path.dirname(os.path.abspath(__file__))
name = 'aaa.xls'
path = path1+'\\'+name
# print(path)
# print(path)

def main(path):
    wb = xlwt.Workbook()
    sheet = wb.add_sheet("2003测试表")
    value = [["名称", "价格", "出版社", "语言"],
             ["如何高效读懂一本书", "22.3", "机械工业出版社", "中文"],
             ["暗时间", "32.4", "人民邮电出版社", "中文"],
             ["拆掉思维里的墙", "26.7", "机械工业出版社", "中文"]]
    for i in range(0, 4):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])
    wb.save(path)
    print("写入数据成功！")
    pass


if __name__ == '__main__':
    main(path)
    pass