#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 16:42
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : getCPUInfo.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com

import psutil
import os
from influxdb import InfluxDBClient
import time,math,random

p1 = psutil.Process(os.getpid())

while True:
    memory_usage_rate = psutil.virtual_memory().percent #内存占用率
    cpu_useage_rate = psutil.cpu_percent(interval=1.0)  #CPU占用率

    json_body = [
        {
            "measurement":"cpu_load_short",
            "tags":{
                "host":"server01",
                "region":"us-west"
            },
            "fields":{
                "cpu":cpu_useage_rate,
                "memory":memory_usage_rate
            }
        }
    ]

    client = InfluxDBClient('localhost',8086,'liugang9','liugang9','java.exe')
    client.create_database()
    client.write_points(json_body)
    time.sleep(2)