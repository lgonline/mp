#/usr/bin/python
__author__ = 'hcm'

import turtle



if __name__ == "__main__":
    t = turtle.Pen()
    for x in range(1,19):
        t.forward(100)
        if x % 2 == 0:
            t.left(175)
        else:
            t.left(225)