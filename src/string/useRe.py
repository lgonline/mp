__author__ = 'Administrator'

import re

str = "Hello World"
print("str is : ",str)
print(re.findall(r"\b\w+\b",str))