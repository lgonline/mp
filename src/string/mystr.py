__author__ = 'Administrator'

import os
import re

file = open("d:\\1.txt")
context = file.read()
message = context.split(" ")
print(context)
print(message)
for info in message:
    print(info)

srcadd = message[0]
print("srcadd is ",srcadd)
requesturl = message[6]
print('requesturl is : ',requesturl)


file.close()