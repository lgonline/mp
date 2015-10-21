#/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'hcm'

from tkinter import *
from src.ballgame.Ball import Ball
from src.ballgame.Paddle import Paddle
import time,random

if __name__ == "__main__":
    tk = Tk()
    tk.title = ("Ball Game")
    tk.resizable(0,0)
    tk.wm_attributes("-topmost",1)

    canvas = Canvas(tk,width=500,height=500,bd=0)
    canvas.pack()
    tk.update()

    #实例化一个球拍
    paddle = Paddle(canvas,'red')
    #实例化一个小球
    ball = Ball(canvas,paddle,'blue')

    while 1:
        #ball.draw()
        #paddle.draw()

        #增加游戏结束的判断,检查小球是否撞到了屏幕的底端
        if ball.hit_button == False:
            ball.draw()
            paddle.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)

    canvas.mainloop()