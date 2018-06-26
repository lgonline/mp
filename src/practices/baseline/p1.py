#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/25 18:30
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : p1.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com

import string
import re

# tomcat_home = input('请输入你的tomcat主目录\n')
# print('你的tomcat主目录是：',tomcat_home)
# check_task = input('请输入你要检查的项目\n1. 检查所有配置项\n2. 检查telnet管理端口配置项\n3. 检查所有配置项\n4. 检查所有配置项\n')


def checkTelnetMgmtPort():
    print('**********telnet管理端口配置项**********')
    # config_file = tomcat_home+'\\conf\\server.xml'
    config_file = 'E:\\Developer\\apache-tomcat-7.0.73\\conf\\server.xml'
    # print(config_file)
    with open(config_file) as files:
        content = files.readlines()
        # <Server port="8005" shutdown="SHUTDOWN">
        connector_conf = re.findall('<Server port="(\d+)" shutdown="(\S+)".*',str(content))
        for content in connector_conf:
            # print(content)
            if content[0] == '8005':
                print('发现tomcat不安全设置：telnet到Tomcat服务器启用默认端口')
                print('安全建议：如确有telnet到tomcat的业务需求，应修改默认端口为20000以上的端口')
            else:
                print('未发现tomcattelnet到Tomcat服务器启用默认端口的不安全设置')

            if content[1] == 'SHUTDOWN':
                print('发现tomcat不安全设置：telnet到Tomcat服务器启用默认口令')
                print(
                    '安全建议：shutdown的属性值的长度、复杂度和定期更新应满足京东关于账号口令的要求。')
            else:
                print('未发现tomcattelnet到Tomcat服务器启用默认端口的不安全设置')

# def main():
#     if check_task == '2':
#         checkTelnetMgmtPort()
#     pass


if __name__ == '__main__':
    # main()
    checkTelnetMgmtPort()
