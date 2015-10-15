__author__ = 'Administrator'

from fun import fun_year

flag = True
while flag:
    year = int(input("please input your year : "))
    if (fun_year.fun_calculator_year(year) == False):
        print("Not a leap year")
        break
    else:
        print("Yes, a leap year")
        continue
else:
    print("it is over.")