__author__ = 'Administrator'

from random import randint

allNums = []
osNums=[]
qsNum=[]
for eachNum in range(10):
    allNums.append(randint(1000,9999))
    allNums.sort()
print(allNums," ")
for i in range(len(allNums)):
    if (allNums[i]%2 == 0):
        osNums.append(allNums[i])
        osNums.sort()
    else:
        qsNum.append(allNums[i])
        qsNum.sort()
print(osNums," ")
print(qsNum," ")


