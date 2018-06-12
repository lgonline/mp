#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/11 19:35
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : portMonitors.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com

import configparser
from .lib.Main import *

NAME, VERSION, AUTHOR, LICENSE = "portMonitor", "V0.1", "330mlcc", "Public (FREE)"

# 满足如下安全需求
# 1、对列表IP进行快速全端口扫描
# 2、周期时间(如每日)增加/减少哪些些端口服务
# 3、开放的端口服务是否存在弱口令风险
# 4、输出所有结果到excel，并发送Email通知

if __name__ == '__main__':
    conf_info = {}
    conf = configparser.ConfigParser()
    conf.read('conf/info.conf')

    conf_info['ip_file'] = conf.get("OPTIONS", "ip_file").strip()
    conf_info['db_user'] = conf.get("OPTIONS", "db_user").strip()
    conf_info['db_pass'] = conf.get("OPTIONS", "db_pass").strip()
    conf_info['type'] = conf.get("OPTIONS", "type").strip()
    conf_info['rate'] = conf.get("Masscan", "rate").strip()
    conf_info['email_user'] = conf.get("Email", "user").strip()
    conf_info['email_pass'] = conf.get("Email", "pass").strip()
    conf_info['target_email'] = conf.get("Email", "target_email").strip()
    conf_info['smtp_server'] = conf.get("Email", "smtp_server").strip()

    main(conf_info)


