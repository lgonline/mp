__author__ = 'Administrator'

def showinfo(name,age,**kw):
    print('name is ',name,'\nage is ',age,'\nother infor :',kw)

def fun1(a,b,c=0,*args,**kw):
    print('a = ',a,', b = ',b,', c = ',c,', args = ',args,', kw = ',kw)

def fun2(a,b,c=0,*,d,**kw):
    print('a = ',a,', b = ',b,', c = ',c,', d = ',d,', kw = ',kw)

if __name__ == "__main__":
    #name = input("Please input the name your wanted.\n")
    #age = int(input('please input the age your wanted.\n'))
    #keyinfo = input('please input the key info your wanted.\n')
    #print(showinfo(name,age,information=keyinfo,job='engineer'))
    #print('--------fun1() & fun2()-----------')
    print(fun1(1,2))
    #print("fun1(1,2,c=3) is : ",fun1(1,2,c=3))
    #print("fun1(1,2,3,'a','b') is : ",fun1(1,2,3,'a','b'))
    #print("fun1(1,2,3,'a','b',x=99) is : ",fun1(1,2,3,'a','b',x=99))
    #print("fun2(1,2,d=99,ext=None) is : ",fun2(1,2,d=99,ext=None) )