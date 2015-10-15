__author__ = 'Administrator'


str1 = "A->B->C->D->E->F"
str2 = "A/B/C/D/E/F"
str3 = "A B C D E F"

print("str1 is : ",str1)
print("str1.split(->) is : ",str1.split("->"))
print("str2 is : ",str2)
print("str2.split(/) is : ",str2.split("/"))
print("str3 is : ",str3)
print("str3.split( ) is : ",str3.split(" "))