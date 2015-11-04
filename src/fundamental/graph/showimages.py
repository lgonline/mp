#/usr/bin/python
__author__ = 'hcm'

from tkinter import *

if __name__ == "__main__":
    tk = Tk()

    cavnes = Canvas(tk,width=500,heigh=500)

    myimage = PhotoImage(file="D:\\JetBrains\\workspaces\\images\\3.gif")
    cavnes.create_image(20,20,anchor=NW,image=myimage)

    cavnes.pack()
    cavnes.mainloop()