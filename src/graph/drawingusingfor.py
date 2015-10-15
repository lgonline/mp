#/usr/bin/python
__author__ = 'hcm'

import turtle

if __name__ == "__main__":
    t = turtle.Pen()

    #draw a square
    for x in range(1,5):
        t.forward(50)
        t.right(90)

    #draw a start
    t.left(180)
    for x in range(1,9):
        t.forward(100)
        t.left(225)

    #draw anothers start
    t.left(60)
    t.forward(50)
    for x in range(1,38):
        t.forward(50)
        t.left(175)

    #draw anothers start
