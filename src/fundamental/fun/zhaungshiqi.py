#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

enable_tracing = True

if enable_tracing:
    debug_log = open("debug.log","w")

'''
the package funcation to output the debug information,then call the
init object
'''
def tracers(func):
    if enable_tracing:
        def callf(*args,**kwargs):
            debug_log.write("Calling %s: %s, %s\n",func.__name__,args,kwargs)
            r = func(*args,**kwargs)
            debug_log.write("%s returned s\n",(func.__name__,r))
            return r
        return callf
    else:
        return func

@tracers
def square(x):
    return x * x

tracers(square(10))

#if __name__ == "__main__":
#    square(10)