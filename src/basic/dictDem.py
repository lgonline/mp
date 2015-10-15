__author__ = 'Administrator'

userDictionary={}
for i in range(10):
    for j in range(i+1):
        j += 10
        #pass
    userDictionary.setdefault(i,j)
print(userDictionary)

del(userDictionary[0])
print(userDictionary)

userDictionary.pop(1)
print(userDictionary)

for (k,v) in userDictionary.items():
    print(k,":",v)
#遍历
print(userDictionary.items())

#拷贝
copyUserDictionary = userDictionary.copy()
print(copyUserDictionary)

print(copyUserDictionary.get(3))
