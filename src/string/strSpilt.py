__author__ = 'Administrator'

inputs = input('please input the value your wanted.\n')
lenghts = int(input('please input the length your wanted.\n'))
myinputs = inputs.split(',')
mystr = []
for i in range(lenghts):
    mystr.append(myinputs[i])

print(mystr)