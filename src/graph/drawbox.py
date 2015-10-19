#/usr/bin/python
__author__ = 'hcm'

'''
from tkinter import *


if __name__ == "__main__":
    tk = Tk()
    canvas = Canvas(tk,width=500,height=500)
    canvas.pack()
    canvas.create_rectangle(10,10,50,50)
'''

from tkinter import *

master = Tk()
canvas = Canvas(master,width=500,height=500)

canvas.create_line(0,0,500,500)
canvas.create_rectangle(50,50,200,100)

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