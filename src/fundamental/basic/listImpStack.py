__author__ = 'Administrator'

from random import randint

allnums = []
for i in range(10):
    allnums.append(randint(1000,9999))
print("add component is : ",allnums)

for j in range(len(allnums)):
    print("remove component is : ",allnums.pop())