# -*- coding: utf-8 -*-
# @Time    : 2018/6/1 13:11
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : setup.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com

"""

"""

import sys
from setuptools import setup

setup(
    name = 'my pip-pop',
    version = '1.0.0',
    url = 'https://github.com/kennethreitz/pip-pop',
    scripts = ['bin/pip-deff','bin/pip-grep'],
    classifiers=[

    ]
)

if __name__ == '__main__':
    pass


