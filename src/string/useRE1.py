__author__ = 'Administrator'

import re

p = re.compile(r'\d+')
print("p.findall('one1two2three3four4') is : ",p.findall('one1two2three3four4'))

print("---------------email register system---------------")
username = input("Please input your username.")
password = input("Please input your password.")
pwds3 = input("Please input your password again.")
email = input("Please input your email address.")

regulars = re.match(r"^([a-z0-9A-Z]+[-|\\.]?)+[a-z0-9A-Z]@([a-z0-9A-Z]+(-[a-z0-9A-Z]+)?\.)+[a-z0-9A-Z]{2,}$",email)

if regulars:
    print("your accounts register is successful! your email address is : ",email)
else:
    print("your account is incurrent.")