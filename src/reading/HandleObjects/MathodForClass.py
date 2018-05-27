__author__ = 'Administrator'

class StaticMethodForClass:
    #define a static method
    @staticmethod
    def myStaticMethod():
        print("This is a static method my defined.")

    #define a private method
    def __myPrivateMethod():
        print("This is a private method my defined.")

    #define a normal method
    def myNormalMethod():
        print("This is a normal method my defined.")

    conversion = staticmethod(myNormalMethod())
    conprivate = staticmethod(__myPrivateMethod())