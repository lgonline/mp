__author__ = 'Administrator'

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1,2,3,4,5,6,7,8,9,10)
x = f()
print(x)

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

# fix:
def countDiff():
    fs = []
    def f(n):
        def j():
            return n * n
        return j
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count()
df1,df2,df3 = countDiff()

print('f1()',f1())
print('f2()',f2())
print('f3()',f3())

print('df1()',df1())
print('df2()',df2())
print('df3()',df3())
