__author__ = 'Administrator'

try:
    print('trying...')
    r = 10 / 5
    print('the result is : ',r)
except ZeroDivisionError as e:
    print('the exception was escapted',e)
finally:
    print('finally...')
print('end...')