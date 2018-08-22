__author__ = 'Administrator'

from fundamental.fun import fun_year

def fun_calculator_year(year):
    #result = ''
    flag = True
    if((year%4 == 0) or (year%100 == 0) or (year%400 == 0)):
        #result = "this year is a leap year."
        flag = True
    else:
        #result = "this year is not a leap year."
        flag = False
    return flag

def handleLeapYear():
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