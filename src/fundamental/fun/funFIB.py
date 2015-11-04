__author__ = 'Administrator'

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n = n+1
    return 'done'

if __name__ == '__main__':
    input = int(input('please input the level your wanted.\n'))
    fib(input)