# -*- coding: utf-8 -*-
# @Time    : 2018/6/1 13:24
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : useSetuptoolsSetup.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com

"""

"""

from setuptools import setup,find_packages
"""
其他一些setup.py文件的参数选项：
 python setup.py build     #编译
 #安装
 python setup.py install    
 example: python setup.py install package
 python setup.py sdist      #制作分发包
 python setup.py bdist_wininst    #制作windows下的分发包
 python setup.py bdist_rpm
"""

def main():
    setup(
        name = 'test for setuptools',
        version = '1.0.1',
        # packages = find_packages()
        packages = ['myapp'],    # 包括在安装包内的Python包
        # python setup.py bdist_egg,在当前目录下创建一个egg文件
        # As from https://pypi.python.org/pypi?%3Aaction=list_classifiers
        classifiers = [
            # 'Development Status :: 1 - Planning',
            # 'Development Status :: 2 - Pre-Alpha',
            # 'Development Status :: 3 - Alpha',
            'Development Status :: 4 - Beta',
            # 'Development Status :: 5 - Production/Stable',
            # 'Development Status :: 6 - Mature',
            # 'Development Status :: 7 - Inactive',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: Implementation :: CPython',
            'Programming Language :: Python :: Implementation :: PyPy',
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Topic :: System :: Systems Administration',
        ]
    )
    pass


if __name__ == '__main__':
    main()
