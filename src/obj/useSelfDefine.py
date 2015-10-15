__author__ = 'Administrator'

class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name = %s)' % self.name
    repr__ = __str__

print(Student('Make'))
s = Student('michael')
print(s)

#useing a self-define class to return a object of iterator
class Fib(object):
    def __init__(self):
        #init the two values
        self.a, self.b = 0, 1

    def __iter__(self):
        #the instance is object for itself, so return itself
        return self

    def __next__(self):
        #calculator the next value
        self.a, self.b = self.b, self.a + self.b
        #the exit condition
        if self.a > 100:
            raise StopIteration()
        #return the next value
        return self.a

for n in Fib():
    print(n)

class Fibs(object):
    def __getitem__(self, n):
        a, b = 1, 1

        for x in range(n):
            a, b = b, a + b
        return a

fs = Fibs()
print(fs[0:5])