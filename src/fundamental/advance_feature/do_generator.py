#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = 'liugang5'

if __name__ == "__main__":
    s = (x * x for x in range(5))
    print(s)
    for x in s:
        print(x)

    #著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到
    #斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易
    #输出斐波那契数列的前N个数
    def fib1(max):
        n, a, b = 0, 0, 1
        while n < max:
            print(b)
            a, b = b, a + b
            n = n + 1
        return 'ok'

    #fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。
    #上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了
    #如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
    def fib2(max):
        n, a, b = 0, 0, 1
        while n < max:
            yield b
            a, b = b, a + b
            n = n + 1
        return 'done'

    #generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行

    f = fib2(10)
    print('fib(10):', f)
    for x in f:
        print(x)

    # call generator manually:
    g = fib2(5)
    while 1:
        try:
            x = next(g)
            print('g:', x)
        except StopIteration as e:
            print('Generator return value:', e.value)
            break