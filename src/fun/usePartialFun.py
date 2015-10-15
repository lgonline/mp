__author__ = 'Administrator'

x = int('12345')
print("int('12345') is : ",x)

y = int('12345',base=8)
print("int('12345',base=8) is : ",y)

z = int('12345',base=16)
print("int('12345',base=16) is : ",z)

def int10to2(x,base=2):
    return int(x,base)

print('int10to2(10000000) is : ',int10to2('10000000'))
print('int10to2(00000100) is : ',int10to2('00000100'))
print('int10to2(00000010) is : ',int10to2('00000010'))