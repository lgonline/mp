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
@file: handleNetcatDemo.py
@time: 18-8-31 上午12:35 
Description: 
"""

import sys
import socket
import getopt
import threading
import subprocess

listen = False
command = False
upload = False

excute = ""
target = ""
upload_destination = ""
port = ""

def run_command(command):
    command = str(command).rstrip()
    try:
        print('the command is : ',command)
        output = subprocess.check_output(command,stderr = subprocess.STDOUT)
    except:
        output = "Failed to execute command.\n"

    return output


def client_handler(client_socket):
    global upload
    global execute
    global command

    if len(upload_destination):
        file_buffer = ""
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            else:
                file_buffer += data

        try:
            file_descriptor = open(upload_destination,'wb')
            file_descriptor.write(file_buffer)
            file_descriptor.close()
            client_socket.send(str.encode('Successfully daved file to %s \n' % upload_destination))
        except:
            client_socket.send(str.encode("failed to dave file to %s \n" % upload_destination))

    if len(execute):
        output = run_command(execute)
        client_socket.send(str.encode(output))

    if command:
        while True:
            client_socket.send(str.encode('<BHP:#>'))
            cmd_buffer = ""
            cmd_buffer = str.encode(cmd_buffer)
            while '\n' not in bytes.decode(cmd_buffer):
                cmd_buffer += client_socket.recv(1024)
            response = run_command(cmd_buffer)
            print('response is : ',response)
            client_socket.send(response)




def main():
    pass


if __name__ == '__main__':
    main()
    pass 
    
    