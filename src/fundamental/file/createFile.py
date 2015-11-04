__author__ = 'Administrator'

import os

filepath = input("Please input your file path : ")
filename = input("Please input your file name : ")
file = filepath+":\\\\"+filename+".txt"
print(file)
if os.path.isfile(file):
    print("file is existing")
else:
    f = open(file,mode="w",encoding="UTF-8")
    print("file",file," has been created.")