#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/20 18:27
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : searchFiles.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com

"""

"""

import os

dirs = 'E:/LIUGANG9/test'                           #文件夹目录
filelists = os.listdir(dirs)                        #得到文件夹下的所有文件名称
files = []
def main():
    for filelist in filelists:                      #遍历文件夹
        if os.path.isdir(filelist) == False:        #判断是否是文件夹，不是文件夹才打开
            # 打开文件
            tmp_fodles = open(dirs+'/'+filelist)
            print(tmp_fodles)
            iter_files = iter(tmp_fodles)                #创建迭代器
            results = ''
            for filename in iter_files:             #遍历文件，一行行遍历，读取文本
                results = results + filename
            files.append(results)
    pass
    print(files)

def processDirectory(args,dirname,filenames):
    print('processDirectory',dirname)
    for filename in filenames:
        print('File ',filename)

def GetFileList(dir, fileList):
    # newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir)

    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            #如果需要忽略某些文件夹，使用以下代码
            #if s == "xxx":
                #continue
            newDir = os.path.join(dir,s)
            GetFileList(newDir, fileList)

    return fileList

if __name__ == '__main__':
    # main()
    list = GetFileList(dirs, [])
    for e in list:
        print(e)
    # pass