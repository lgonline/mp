__author__ = 'Administrator'

class MyAttribute(object):
    def __init__(self):
        self.default = 0.0
        self.age = 20
        self.member = 21

    def __getattribute__(self, name):
        if name == "test":
            print("When the test property was called, __getattribute__ is : ",name)
            return self.test
        else:
            print("When the test property was not called, the output is : ",name)
            return object.__getattribute__(self,name)

    def __getattr__(self, name):
        print("the output is ",name," , when use the __getattr__ method")
        print("the default values is : ",self.default)
        return self.default