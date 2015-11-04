__author__ = 'Administrator'

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


