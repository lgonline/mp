__author__ = 'Administrator'

from fundamental.obj import Teacher
from fundamental.obj import Student

teacher = Teacher("liugang",40,"Beijing","travel",3000)
students = Student("liupeicheng",5,"Beijing","display",85)
members = [teacher,students]
for member in members:
    member.tell()
