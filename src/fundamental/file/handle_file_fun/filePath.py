__author__ = 'Administrator'

import os
import re

flag = True

while flag:
    filepath = input("Please input your file path : \n")
    if (filepath == 'c') or (filepath == 'd'):
        filename = input("Please input your file name : \n")
    else:
        print("your input file path is incorrect.")
    file = filepath+":\\\\"+filename+".txt"
    if os.path.isfile(file):
        print("file is existing")
    else:
        myfile = open(file,mode="w",encoding="UTF-8")

    content = input("please input you wanted.\n")
    myfile = open(file,"a+")
    myfile.write(content)

    openfile = open(file)
    filecontent = openfile.readlines()
    for line in filecontent:
        print(line)

    operation  = int(input("do you want next step?\n 1.yes\n2. no\n"))
    if operation == 1:
        continue
    elif operation == 2:
        print("the project is quit.")
        flag = False
    else:
        break
