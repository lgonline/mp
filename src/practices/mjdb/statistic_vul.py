#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 12:02
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : statistic_vul.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com

"""

"""

import xlwt

if __name__ == '__main__':
    # 创建一个Workbook对象，这就相当于创建了一个Excel文件
    excel_book = xlwt.Workbook(encoding='utf-8', style_compression=0)

    # 创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格。
    # 在电脑桌面右键新建一个Excel文件，其中就包含sheet1，sheet2，sheet3三张表
    data_sheet = excel_book.add_sheet('vul_data', cell_overwrite_ok=True)
    # 其中的'0-行, 0-列'指定表中的单元，'EnglishName'是向该单元写入的内容
    # data_sheet.write(0, 1, 'Name')
    with open('vul.txt', 'r',encoding='utf-8') as files:
        lines = files.readlines()
        print(len(lines))

    for i in range(len(lines)):
        data_sheet.write(i, 0, lines[i])

    excel_book.save('e:\\test1.xls')

    files.close()