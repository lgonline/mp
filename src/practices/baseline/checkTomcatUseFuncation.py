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
import xmltodict
import zipfile

TOMCAT_HOME = 'E:\\Developer\\apache-tomcat-7.0.73'
tomcat_server_config = TOMCAT_HOME+'\\conf\\server.xml'
admin_console = TOMCAT_HOME+'\\webapps\\admin'
manager_console = TOMCAT_HOME+'\\webapps\\manager'
tomcat_user = TOMCAT_HOME+'\\conf\\tomcat-users.xml'
web_config = TOMCAT_HOME+'\\conf\\web.xml'
lib_config = TOMCAT_HOME+'\\conf\\catalina.jar'
print(lib_config)

def checkTelnetPort():
    print('***********开始检查telnet到Tomcat服务器的默认端口************')
    with open(tomcat_server_config) as files:
        content = files.readlines()
        connector_conf = re.findall('<Server port="(\d+)" shutdown="(\S+)">',str(content))
        # print(connector_conf)
        for telnetport in connector_conf:
            if telnetport[0] == '8005':
                print('发现tomcat不安全设置：telnet到Tomcat服务器启用默认端口')
                print('安全建议：如确有telnet到tomcat的业务需求，应修改默认端口为20000以上的端口')
            else:
                print('未发现tomcat不安全设置：telnet到Tomcat服务器启用默认端口')
            if telnetport[1] == 'SHUTDOWN':
                print('发现tomcat不安全设置：telnet到Tomcat服务器启用默认口令')
                print('安全建议：如确有telnet到tomcat的业务需求，应修改shutdown服务的默认属性值，属性值的长度、复杂度和定期更新应满足京东关于账号口令的要求')
            else:
                print('未发现tomcat不安全设置：telnet到Tomcat服务器启用默认口令')

def checkAJPPort():
    print('***********开始检查tomcat和apache的ajp连接端口************')
    with open(tomcat_server_config) as files:
        content = files.readlines()
        connector_conf = re.findall('<Connector port="(\d+)" protocol="(\S+) redirectPort="(\d+)"\/>', str(content))
        # print(connector_conf)
        for apjport in connector_conf:
            if apjport[0] == '8009':
                print('发现tomcat不安全设置：ajp连接默认端口')
                print(
                '安全建议：如确有tomcat和apache的ajp连接的业务需求，应修改默认端口为20000以上的端口')

def checkMgmtConfig():
    print('***********开始检查管理台的默认设置************')


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

def checkDefaultErrorPage():
    print('***********开始检查tomcat错误页面的设置************')
    with open(web_config) as webconfigfile:
        config_content = webconfigfile.readlines()

        if re.search('<error-page>',str(config_content)) is None:
            print('发现tomcat不安全设置：未进行返回错误页面的的配置')
            print('安全建议：在tomcat的web.xml中配置自定义的错误跳转页面')

        else:
            results = re.findall(r'<error-code>(\d+)</error-code>', str(config_content))
            if '404' not in results:
                print('发现tomcat不安全设置：未进行404错误的返回处理配置')
            else:
                print('未发现tomcat对404错误页面设置的不安全配置')

            if '500' not in results:
                print('发现tomcat不安全设置：未进行500错误的返回处理配置')
            else:
                print('未发现tomcat对500错误页面设置的不安全配置')

def checkListFolder():
    print('***********开始检查tomcat列目录的的安全设置************')

    with open(web_config) as wb:
        docs = xmltodict.parse(wb.read())
        servlet_content = docs['web-app']['servlet']

        if '(\'param-name\', \'listings\'), (\'param-value\', \'false\')' in str(servlet_content):
            print('发现tomcat不安全设置：列出Web目录下的文件')
        else:
            print('未发现tomcat不安全设置：列出Web目录下的文件')

def checkRunerAuthentication():
    print('***********开始检查tomcat的运行权限设置************')

def checkAutoDeploy():
    print('***********开始检查tomcat的war自动部署设置************')
    with open(tomcat_server_config) as wbconfig:
        config_content = wbconfig.readlines()
        results = re.findall(r'<Host appBase="(\S+)" autoDeploy="(\S+)" name="(\S+)" unpackWARs="(\S+)">',str(config_content))
        for result in results:
            if result[1] == 'true':
                print('发现tomcat不安全设置：未关闭war自动部署')
            else:
                print('已关闭war自动部署')

def checkOpenTomcatLog():
    print('***********开始检查tomcat开启日志记录的设置************')
    with open(tomcat_server_config) as wbconfig:
        config_content = wbconfig.readlines()
        if 'org.apache.catalina.valves.AccessLogValve' in re.findall(r'<Valve className="(\S+)" directory=".*', str(config_content)):
            print('已开启Tomcat日志记录')
        else:
            print('发现tomcat不安全设置：未开启Tomcat日志记录')

def checkTomcatVersionInfo():
    print('***********开始检查tomcat隐藏版本信息的设置************')
    with zipfile('E:\\Developer\\apache-tomcat-7.0.73\\lib\\catalina.jar') as wbconfig:
        # with wbconfig.open('\\org\\apache\\catalina\\util\\ServerInfo.properties') as myfiles:
        #     print(myfiles.read())
        pass


if __name__ == '__main__':
    print('***********开始检查tomcat安全配置************')
    checkTomcatVersionInfo()
