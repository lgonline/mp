__author__ = 'Administrator'

str1 = "hello, lgonline, welcome to here."
print("str1 is : ",str1)
print("str1.capitalize() is : ",str1.capitalize())
changes = str1.maketrans('abcdef','123456')
print(str1,'was changed : ',str1.translate(changes))
