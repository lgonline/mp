__author__ = 'Administrator'

from fundamental.basic import AgeCalculator

print("hi, xiaoming, please input your age: ")
xiaoming=float(input())
print("hi, xiaoming, please input your age in the further: ")
furtherage=float(input())
print("hi, xiaoming, please input your father's age : ")
fatherage=float(input())


print("hi, xiaoming, your age is ",xiaoming,"and when your age is ",furtherage," , then your father age is : ",
      AgeCalculator.checkAge(xiaoming,furtherage,fatherage))
