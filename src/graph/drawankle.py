#/usr/bin/python
__author__ = 'hcm'

from tkinter import *

if __name__ == "__main__":
    tk = Tk()

    canvas = Canvas(tk,width=500,height=500)
    canvas.create_polygon(10,10,100,10,100,110,fill="",outline="black")

    canvas.pack()
    canvas.mainloop()