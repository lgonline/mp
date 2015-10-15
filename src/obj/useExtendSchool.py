__author__ = 'Administrator'

class School:
    def __init__(self,name,age,addr,hoppy):
        self.name = name
        self.age = age
        self.addr = addr
        self.hoppy = hoppy

    def tell(self):
        print("Name is ",self.name," , age is ",self.age," , addr is ",self.addr," and hoppy is ",self.hoppy)

class Teacher(School):
    def __init__(self,name,age,addr,hoppy,salary):
        School.__init__(self,name,age,addr,hoppy)
        self.salary = salary

    def tell(self):
        School.tell(self)
        print("my salary is ",self.salary)

class Student(School):
    def __init__(self,name,age,addr,hoppy,marks):
        School.__init__(self,name,age,addr,hoppy)
        self.marks = marks

    def tell(self):
        School.tell(self)
        print("my marks is ",self.marks)
