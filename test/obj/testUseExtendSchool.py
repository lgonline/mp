__author__ = 'Administrator'

from obj.useExtendSchool import Teacher
from obj.useExtendSchool import Student

teacher = Teacher("liugang",40,"Beijing","travel",3000)
students = Student("liupeicheng",5,"Beijing","display",85)
members = [teacher,students]
for member in members:
    member.tell()
