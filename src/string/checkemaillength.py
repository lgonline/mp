__author__ = 'Administrator'

email = input("Please input your email address.")
if ((email.rfind("@") > 18 ) or (email.rfind("@") < 6)):
    print("your email lenght is incurrent.")
    email = input("please input your email address.")
else:
    print("continue...")