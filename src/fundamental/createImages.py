#/usr/bin/python
__author__ = 'hcm'

from tkinter import *
import time
import turtle

def hello():
    print("hello world!!!")

def handleBasicImage():
    tk = Tk()

    canvas = Canvas(tk, width=500, height=500)
    canvas.create_polygon(10, 10, 100, 10, 100, 110, fill="", outline="black")

    canvas.pack()
    canvas.mainloop()

def handleImage2():
    tk = Tk()

    cavnes = Canvas(tk,width=500,height=500)
    cavnes.create_polygon(10,10,10,60,50,35)

    cavnes.pack()


    for x in range(0,60):
        cavnes.move(1,5,0)
        tk.update()
        time.sleep(0.05)

    cavnes.mainloop()

def drawBoxImages():
    master = Tk()
    canvas = Canvas(master, width=500, height=500)

    canvas.create_line(0, 0, 500, 500)
    canvas.create_rectangle(50, 50, 200, 100)

    canvas.pack()

    canvas.mainloop()

    '''
    Label(master, text="First").grid(row=0, sticky=W)
    Label(master, text="Second").grid(row=1, sticky=W)

    e1 = Entry(master)
    e2 = Entry(master)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    mainloop()
    '''

def drawButton():
    top = Tk()
    btn = Button(top, text="click me", command=hello)
    btn.pack()
    top.mainloop()

def drawCars():
    t = turtle.Pen()
    t.color(1,0,0)
    t.begin_fill()
    t.forward(100)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.end_fill()

    t.color(0,0,0)
    t.up()
    t.forward(10)
    t.down()
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    t.setheading(0)
    t.up()
    t.forward(90)
    t.right(90)
    t.forward(10)
    t.setheading(0)
    t.begin_fill()
    t.down()
    t.circle(10)
    t.end_fill()

def drawCycle():
    tk = Tk()

    canvas = Canvas(tk, width=500, height=500)

    canvas.create_arc(10, 10, 200, 80, extent=45, style=ARC)
    canvas.create_arc(10, 80, 200, 160, extent=90, style=ARC)
    canvas.create_arc(10, 160, 200, 240, extent=135, style=ARC)
    canvas.create_arc(10, 240, 200, 320, extent=180, style=ARC)
    canvas.create_arc(10, 320, 200, 400, extent=359, style=ARC)

    canvas.pack()
    canvas.mainloop()

def drawImages2():
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

def drawWords():
    tk = Tk()

    canvas = Canvas(tk,width=500,height=500)
    canvas.create_text(100,100,text="Hello World!!!")
    canvas.create_text(100,200,text="python, i love you",font=('Courier',10))

    canvas.pack()
    canvas.mainloop()

def drawImages3():
    t = turtle.Pen()
    for x in range(1, 19):
        t.forward(100)
        if x % 2 == 0:
            t.left(175)
        else:
            t.left(225)

if __name__ == "__main__":
    drawButton()