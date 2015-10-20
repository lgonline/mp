#/usr/bin/python
__author__ = 'hcm'

from tkinter import *
import random,time

class Ball:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        #add some function to meet the requirement of reflect
        #self.x = 0
        #self.y = -1
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()


    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        #create parameter called pos to distribute value
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3
'''
tk = Tk()
tk.title = "Game"
tk.resizable(0,0) #the windows size cannot chage in width and height
tk.wm_attributes("-topmost",1)

cavnes = Canvas(tk,width=500,height=500,bd=0)
cavnes.pack()
tk.update()

ball = Ball(cavnes,'blue')

while 1:
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.02)

cavnes.mainloop()
'''