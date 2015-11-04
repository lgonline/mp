#/usr/bin/python
__author__ = 'hcm'

from tkinter import *
import time

if __name__ == "__main__":
    tk = Tk()

    cavnes = Canvas(tk,width=500,height=500)
    cavnes.create_polygon(10,10,10,60,50,35)

    cavnes.pack()


    for x in range(0,60):
        cavnes.move(1,5,0)
        tk.update()
        time.sleep(0.05)

    cavnes.mainloop()