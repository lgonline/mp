#/usr/bin/python
__author__ = 'hcm'

from tkinter import *
from src.ballgame.Ball import Ball
from src.ballgame.Paddle import Paddle
import time,random

if __name__ == "__main__":
    tk = Tk()
    tk.title = "Game"
    tk.resizable(0,0) #the windows size cannot chage in width and height
    tk.wm_attributes("-topmost",1)

    cavnas = Canvas(tk,width=500,height=500,bd=0)
    cavnas.pack()
    tk.update()

    ball = Ball(cavnas,'blue')
    paddle = Paddle(cavnas,"red")

    while 1:
        ball.draw()
        paddle.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.02)

    cavnas.mainloop()