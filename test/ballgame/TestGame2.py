#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

from tkinter import *
from test.ballgame.TestPaddle import Paddle
from test.ballgame.TestBall import Ball
import random
import time

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')

while 1:
    ball.draw()
    paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)