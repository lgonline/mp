#/usr/bin/python
__author__ = 'hcm'

from tkinter import *

if __name__ == "__main__":
    tk = Tk()

    canvas = Canvas(tk,width=500,height=500)
    canvas.create_text(100,100,text="Hello World!!!")
    canvas.create_text(100,200,text="python, i love you",font=('Courier',10))

    canvas.pack()
    canvas.mainloop()