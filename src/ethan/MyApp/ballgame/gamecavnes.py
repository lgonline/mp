#/usr/bin/python
__author__ = 'hcm'

from tkinter import *

if __name__ == "__main__":
    tk = Tk()
    tk.title = "Game"
    #tk.resizable(0,0) #the windows size cannot chage in width and height
    #tk.wm_attributes("-topmost",1)

    cavnes = Canvas(tk,width=500,height=500,bd=0)
    cavnes.pack()
    tk.update()

    #ball = Ball(cavnes,'blue')

    #while 1:
    #    ball.draw()
    #    tk.update_idletasks()
    #    tk.update()
    #    time.sleep(0.02)
    print("ok")

    cavnes.mainloop()