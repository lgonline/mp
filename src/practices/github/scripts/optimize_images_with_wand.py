#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/19 15:47
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : optimize_images_with_wand.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com

"""
优化图片

"""

import os,fnmatch
#Python图片处理库Wand
from wand.image import Image
#hurry.filesize a simple Python library that can take a number of bytes and returns a human-readable string with the size in it, in kilobytes (K), megabytes (M), etc.
from hurry.filesize import size

PATH = 'E:\\Developer\\1-Books\\11-Flask\从零开始搭建论坛（三）：Flask框架简单介绍 - 51CTO.COM_files'
Targets = '*.png'

def get_imges_file(filepath,targets):
    matches = []
    if os.path.exists(filepath):
        for root,dirs,filenames in os.walk(filepath):
            for filename in fnmatch.filter(filenames,targets):
                matches.append(os.path.join(filepath,filename))
        if matches:
            print('{} files was found.'.format(len(matches)))
            return matches
        else:
            print('no files was found.')
        pass
    else:
        print('sorry that the file is null.')

def get_total_size(list_of_image_name):
    total_size = 0
    for image_name in list_of_image_name:
        total_size += os.path.getsize(image_name)
    return size(total_size)

def resize_images(list_of_image_name):
    print('optimizing....\n')
    for index,image_name in enumerate(list_of_image_name):
        with open(image_name) as files:
            image_binary = files.read()

        with Image(blob=image_binary) as img:
            if img.height >= 600:
                img.transform(resize='x600')
                img.save(filename=image_name)
    print('optimization complete.')
    pass


if __name__ == '__main__':
    all_images = get_imges_file(PATH,Targets)
    resize_images(all_images)
    get_imges_file(PATH,Targets)
