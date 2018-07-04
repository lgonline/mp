#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/28 14:54
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : readFileToExcel.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com
# @Description: 
#   
#   

import csv
import re

def main():
    out = open('vul.csv','w',newline='')
    csv_write = csv.writer(out,dialect='excel')

    with open('vul2.txt',encoding='utf-8') as files:
        contents = files.readlines()
        for content in contents:
            rows = re.findall(r'(\S+)\s{4}(\S+)\s{4}(.*)',content)
            # print(rows)
            for row in rows:
                csv_write.writerow(row)
        print("write over")
    pass

if __name__ == '__main__':
    main()
    pass