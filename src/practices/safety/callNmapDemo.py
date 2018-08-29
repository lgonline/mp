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
@file: callNmapDemo.py\
@time: 18-8-8 下午11:39 
Description: 
"""

import nmap
import sys

print('[+] nmap scanning...')

def main(sbg):
    nmap_port_scan = nmap.PortScannner()
    nmap_port_scan(sbg,'22')

    for host in nmap_port_scan.all_hosts():
        if nmap_port_scan[host].has_tcp(22):
            state = nmap_port_scan[host]['tcp'][22]['state']
            if state == 'open':
                print('[*] The open 2 ip in : ',host)
    pass


if __name__ == '__main__':
    main(sys.argv)
    pass 
    
    