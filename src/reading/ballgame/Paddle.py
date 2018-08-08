# encoding: utf-8
#/usr/bin/python

__author__ = 'hcm'

from tkinter import *
import time

class Paddle:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill=color)    #调用create_rectangle
        self.canvas.move(self.id,250,400)
        #让球拍移动，，用事件绑定吧左右方向绑定到Paddle类的新函数上，按左键，变量x设定为-2（左移），按右键，x=2（右移）
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        #增加两行代码吧正确的按键绑定到函数上，turn_left绑定左方向键，事件名keyPress-left，右键keyPress-Right
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self):
        self.canvas.move(self.id,self.x,0)  #用画布的move函数在变量的x方向上移动球拍，，得到球拍的坐标来判断是否撞到了屏幕的左右边界
        pos = self.canvas.coords(self.id)
        #球拍不能像球一样弹回来，所以，小于等于零时，x设置为0
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self,evt):
        self.x = -2

    def turn_right(self,evt):
        self.x = 2
