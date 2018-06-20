#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/20 12:11
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : checkMyEnv.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com

"""
Pass in a config file based on your environment.
Example:
import check_my_environment
class Main:
    def __init__(self, configFile):
        pass
    def process(self):
        print("ok")
if __name__ == "__main__":
    m = Main(some_script.CONFIGFILE)
    m.process()
"""

import os,sys

ENVIRONMENT = "development"
CONFIGFILE = None

def main():
    my_dirs = os.path.abspath(__file__)
    return{
        "development":"{}/../config/development.cfg".format(my_dirs),
        "staging": "{}/../config/staging.cfg".format(my_dirs),
        "production": "{}/../config/production.cfg".format(my_dirs)
    }.get(ENVIRONMENT,None)
    pass

CONFIGFILE = main()

if CONFIGFILE is None:
    sys.exit('Configuration error! Unknown environment set. Edit config.py and set appropriate environment')

print("Config file: {}".format(CONFIGFILE))

if not os.path.exists(CONFIGFILE):
    sys.exit("Configuration error! Config file does not exist")

print("Config ok ....")

if __name__ == '__main__':
    # main()
    mydir = os.path.abspath(__file__)
    mydir1 = "./../../../../test/practices/github"
    if os.path.isfile(mydir1):
        print('have')
    else:
        print('have not')
    # print(os.path.abspath(mydir1))
    # print(mydir)
