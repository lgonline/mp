__author__ = 'Administrator'

from obj.MathodForClass import StaticMethodForClass

if __name__ == "__main__":
    mysm = StaticMethodForClass()
    print("mysm.myStaticMethod() is :---------------- ")
    mysm.myStaticMethod()
    print("StaticMethodForClass.myStaticMethod() is :---------------- ")
    StaticMethodForClass.myStaticMethod()
    print("StaticMethodForClass.conversion is : ---------------")
    StaticMethodForClass.conversion
    print("mysm.conversion is : ------------------")
    mysm.conversion
    print("StaticMethodForClass.conprivate is :---------------- ")
    StaticMethodForClass.conprivate
    print("mysm.conprivate is : ------------------")
    mysm.conprivate
