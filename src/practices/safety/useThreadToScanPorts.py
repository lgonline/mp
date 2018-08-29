#!/usr/bin/env python  
# -*- coding: utf-8 -*-

""" 
@version: v1.0 
@author: 330mlcc 
@Software: PyCharm
@license: Apache Licence  
@Email   : mlcc330@hotmail.com
@contact: 3323202070@qq.com
@site:  
@software: PyCharm 
@file: useThreadToScanPorts.py
@time: 18-8-14 下午8:57 
Description: 
"""

import nmap
import logging
import threading,time,queue
import sys
import os
import optparse
from IPy import IP


logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] %(levelname)s: %(message)s",
    filename = 'result_port.txt',
    filemode = 'w'
)

class scan():
    def __init__(self,cidr,threads_num,file_source,ports):
        self.threads_num = threads_num
        self.ports = ports
        self.IPs = queue.Queue()
        if file_source == None:
            self.cidr = IP(cidr)
            for ip in self.cidr:
                ip = str(ip)
                self.IPs.put(ip)
        else:
            pass


def main():
    pass


if __name__ == '__main__':
    main()
    pass 
    
    