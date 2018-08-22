#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = 'liugang5'

def handleIter2():
    def g():
        yield 1
        yield 2
        yield 3

    print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], Iterable))
    print('Iterable? \'abc\':', isinstance('abc', Iterable))
    print('Iterable? 123:', isinstance(123, Iterable))
    print('Iterable? g():', isinstance(g(), Iterable))

    print('Iterator? [1, 2, 3]:', isinstance([1, 2, 3], Iterator))
    print('Iterator? iter([1, 2, 3]):', isinstance(iter([1, 2, 3]), Iterator))
    print('Iterator? \'abc\':', isinstance('abc', Iterator))
    print('Iterator? 123:', isinstance(123, Iterator))
    print('Iterator? g():', isinstance(g(), Iterator))

    # iter list:
    print('for x in [1, 2, 3, 4, 5]:')
    for x in [1, 2, 3, 4, 5]:
        print(x)

    print('for x in iter([1, 2, 3, 4, 5]):')
    for x in iter([1, 2, 3, 4, 5]):
        print(x)

    print('next():')
    it = iter([1, 2, 3, 4, 5])
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))

    d = {'a': 1, 'b': 2, 'c': 3}

    # iter each key:
    print('iter key:', d)
    for k in d.keys():
        print('key:', k)

    # iter each value:
    print('iter value:', d)
    for v in d.values():
        print('value:', v)

    # iter both key and value:
    print('iter item:', d)
    for k, v in d.items():
        print('item:', k, v)

    # iter list with index:
    print('iter enumerate([\'A\', \'B\', \'C\']')
    for i, value in enumerate(['A', 'B', 'C']):
        print(i, value)

    # iter complex list:
    print('iter [(1, 1), (2, 4), (3, 9)]:')
    for x, y in [(1, 1), (2, 4), (3, 9)]:
        print(x, y)

def handleTuiExpress():
    L1 = ['Hello', 'World', 18, 'Apple', None]
    L2 = [s.lower() for s in L1 if isinstance(s, str) is True]
    print(L2)

def handleSlice():
    L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

    print('L[0:3] =', L[0:3])
    print('L[:3] =', L[:3])
    print('L[1:3] =', L[1:3])
    print('L[-2:] =', L[-2:])

    R = list(range(100))
    print('R[:10] =', R[:10])
    print('R[-10:] =', R[-10:])
    print('R[10:20] =', R[10:20])
    print('R[:10:2] =', R[:10:2])
    print('R[::5] =', R[::5])

def handleGenerator():
    s = (x * x for x in range(5))
    print(s)
    for x in s:
        print(x)

    # 著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到
    # 斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易
    # 输出斐波那契数列的前N个数
    def fib1(max):
        n, a, b = 0, 0, 1
        while n < max:
            print(b)
            a, b = b, a + b
            n = n + 1
        return 'ok'

    # fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。
    # 上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了
    # 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
    def fib2(max):
        n, a, b = 0, 0, 1
        while n < max:
            yield b
            a, b = b, a + b
            n = n + 1
        return 'done'

    # generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行

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

if __name__ == "__main__":
    handleIter2()