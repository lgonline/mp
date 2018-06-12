#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/11 19:53
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : Log.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com

import logging
import logging.handlers

NAME, VERSION, AUTHOR, LICENSE = "portMonitor", "V0.1", "330mlcc", "Public (FREE)"

class LogInfo:
    def __init__(self,logfile):
        self.logfile = logfile

        logging.basicConfig(
            level = logging.INFO,
            format = '%(asctime)s - %(name)s - %(message)s'
        )

        self.logger = logging.getLogger('LogInfo')
        fh = logging.FileHandler(self.log_file)
        fh.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

    def infostring(self,infostring):
        self.logger.info(infostring)