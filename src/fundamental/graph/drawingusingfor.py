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
    t.left(160)
    t.forward(150)
    for x in range(1,60):
        t.forward(150)
        t.left(275)

    #draw anothers start
