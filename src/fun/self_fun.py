__author__ = 'Administrator'

def power(x,n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

if __name__ == "__main__":
    x = int(input('please input the first parameter : '))
    n = int(input('please input the second parameter : '))
    a = power(x,n)
    print(a)