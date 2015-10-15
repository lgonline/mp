#/usr/bin/python
__author__ = 'hcm'

from tkinter import *

def hello():
    print("hello world!!!")

if __name__ == "__main__":
    top = Tk()
    btn = Button(top,text="click me",command=hello)
    btn.pack()
    top.mainloop()