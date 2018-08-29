__author__ = 'Administrator'

userTuple1=(1,2,3,4,5)
userTuple2=(6,7,8,9,0)
userTuple=(userTuple1,userTuple2)

for i in range(len(userTuple1)):
    print(userTuple1[i],end="")

print()
for j in range(len(userTuple2)):
    print(userTuple2[j],end="")
print()
for k in range(len(userTuple)):
    for l in range(len(userTuple[k])):
        print(userTuple[k][l],end="")
print()
print("----an other function------")
