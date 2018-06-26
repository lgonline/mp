#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/25 17:05
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : checkTomcat.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com

"""

"""

import re,os

def main():
    # tomcat_home = input('Please enter tomcat home your wanted.\n')
    tomcat_home = 'E:\\Developer\\apache-tomcat-7.0.73'
    print(tomcat_home)

    print('***********开始检查tomcat安全配置************')
    print('***********开始检查telnet到Tomcat服务器的默认端口************')
    with open('E:\\Developer\\apache-tomcat-7.0.73\\conf\\server.xml') as files:
        content = files.readlines()
        # print(type(content))
        # print(content)
        connector_conf = re.findall('<Connector port="(\d+)"',str(content))
        # print(connector_conf[1])
        if connector_conf[1] == '8009':
            print('发现tomcat不安全设置：telnet到Tomcat服务器启用默认端口')
            print('安全建议：如确有telnet到tomcat的业务需求，应修改默认端口为20000以上的端口并修改shutdown服务的属性值，另shutdown的属性值的长度、复杂度和定期更新应满足京东关于账号口令的要求')

    print('***********开始检查管理台的默认设置************')
    admin_console = 'E:\\Developer\\apache-tomcat-7.0.73\\webapps\\admin'
    manager_console = 'E:\\Developer\\apache-tomcat-7.0.73\\webapps\\manager'
    tomcat_user = 'E:\\Developer\\apache-tomcat-7.0.73\\conf\\tomcat-users.xml'

    if os.path.exists(admin_console) == True:
        print('发现tomcat不安全设置：admin管理台的默认应用')
    else:
        print('未发现admin管理台的默认应用')

    if os.path.exists(manager_console) == True:
        print('发现tomcat不安全设置：manager管理台的默认应用')
    else:
        print('未发现manager管理台的默认应用')

    with open(tomcat_user) as files:
        content = files.readlines()
        if re.search('<role',str(content)) is not None or re.search('<user', str(content)) is not None:
            print('发现tomcat不安全设置：未对tomcat-users.xml 中所有<role><user>标签进行注释处理')
        else:
            print('未发现对tomcat-users.xml 中所有<role><user>标签进行注释处理')

    print('***********错误页面的设置，否则必须在Tomcat中设定错误页面的属性************')


    pass


if __name__ == '__main__':
    main()
