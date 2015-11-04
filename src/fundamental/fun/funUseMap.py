__author__ = 'Administrator'

from functools import reduce

def f(x):
    return x * x

r = map(f,list(range(10)))

print(list(r))

str = map(str,range(10))
print('str is : ',list(str))

def add(x,y):
    return x + y

print(reduce(add,range(11)))

z = reduce(add,range(11))
print(z)

#print(list(funadd))


str2 = ['admin','LISA','barT']

def normalize(mystr):
    mystr = mystr[0].upper()+mystr[1:].lower()
    return mystr

lists1 = list(map(normalize,str2))
print(list(lists1))

def prod(x,y):
    return x * y

lists2 = []
for i in range(10):
    lists2 = lists2.append(i)
print(i)
print(reduce((prod,lists2)))
