__author__ = 'Administrator'
import pickle
import os
#serialize

d = dict(name='Bob',age=20,score=88)
print(pickle.dumps(d))


mypath = os.path.abspath('.')
print('mypath is : ',mypath)
#filename = input('\nplease input a file name your wanted.\n')
myfile = mypath+'\\222.txt'
#print('myfile is : ',myfile)
#filename = 'please input a file name your wanted.\n'
#file = open('')

#openfile = open(myfile,mode='w',encoding='utf-8')
#openfile.write("The first write is :\n")
#for mycontent in d:
#    openfile.write(mycontent)
#openfile.write('before serialize...')
#openfile.close()
#of = open(myfile,'wb')
#data = pickle.dump(d,of)
of2 = open(myfile,'rb')
#openfile2.write('after anti-serialize...')
fx = pickle.load(of2)
of2.close()
print(fx)

d = dict(name='Bob', age=20, score=88)
data = pickle.dumps(d)
print(data)

reborn = pickle.loads(data)
print(reborn)

