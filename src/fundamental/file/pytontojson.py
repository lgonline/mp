__author__ = 'Administrator'

import json
d = dict(name='Bob',age=20,score=80)
print('d is ',d)
jd = json.dumps(d)
print('format json is : ',jd)
print('anti-resralize is : ',json.loads(jd))

class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student object (%s, %s, %s' % (self.name,self.age,self.score)

s = Student('Bob',20,88)
std_data = json.dumps(s,default=lambda obj: obj.__dict__)
print('Dump Student : ',std_data)
rebuild = json.loads(std_data,object_hook=lambda d: Student(d['name'],d['age'],d['score']))
print(rebuild)