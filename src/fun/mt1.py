__author__ = 'Administrator'

def my1():
    #n = 1
    for n in range(1,20):
        print('init n',n)
        n = n + 2
        print('reuslt n',n)
        #yield n
    #print('after n',n)

func1 = lambda x:x*2
print(func1(5))

def _not_divisible(n):
    return lambda x: x % n > 0

x = _not_divisible(2)
print(x)
#my1()