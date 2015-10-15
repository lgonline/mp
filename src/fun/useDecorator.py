__author__ = 'Administrator'

import functools

def log(func):
    def wrapper(*args,**kw):
        print('call %s()' % func.__name__)
        return func(*args,**kw)
    return wrapper

def logs(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s()' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator


@log
def printNow():
    print('printNow() 2015-3-25')

@logs('execute')
def printNows():
    print('printNows() 2015-3-25')

#printNow()
#printNows()

def benginend(func):
    def showMessage(*args,**kw):
        print('bengin call %s' % func.__name__)
        ret = func(*args,**kw)
        print('end call %s' % func.__name__)
        return ret
    return  showMessage


def myLogs(text):
    def decorators(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            if len(text) == 0:
                print('%s() : ' % func.__name__)
            else:
                print('%s %s() : ' % (text[0],func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorators

@benginend
def myFun():
    print('call my function')

myFun()
