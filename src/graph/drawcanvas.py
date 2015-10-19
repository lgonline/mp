#/usr/bin/python
__author__ = 'hcm'

from tkinter import *


if __name__ == "__main__":
    top = Tk()
    canvas = Canvas(top,width=500,height=500)
    canvas.pack()
    canvas.create_line(0,0,500,500)