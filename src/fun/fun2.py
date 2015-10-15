__author__ = 'Administrator'

import math

def quadratic(a,b,c):
    if not isinstance(a,int):
        raise TypeError('bad operand type for the parameter of a')
    if not isinstance(b,int):
        raise TypeError('bad operand type for the parameter of b')
    if not isinstance(c,int):
        raise TypeError('bad operand type for the parameter of c')

    x = (b*b)-(4*a*c)
    if x < 0:
        return "the equation is not root"
    elif x == 0:
        return (-b)/(2*a)
    else:
        return (-b+math.sqrt(x))/(2*a),(-b-math.sqrt(x))/(2*a)

if __name__ == "__main__":
    a = int(input('please input the first data you wanted : '))
    b = int(input('please input the second data you wanted : '))
    c = int(input('please input the thired data you wanted : '))
    print(quadratic(a,b,c))