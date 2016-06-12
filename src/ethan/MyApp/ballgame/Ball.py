#/usr/bin/python
__author__ = 'hcm'

import random


class Ball:
    #def __init__(self,canvas,color):
    #修改init参数，加上球拍
    def __init__(self,canvas,paddle,color):
        self.canvas = canvas    #把球拍的paddle参数赋值给对象变量paddle
        self.paddle = paddle    #调用create_oval函数，调用左上角的x,y坐标和右下角的x,y坐标
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)   #把圆形移动到画布的中心
        starts = [-3,-2,-1,1,2,3]   #创建变量starts，它是一个由6个数字组成的列表
        random.shuffle(starts)  #random.shuffle混排starts
        self.x = starts[0]  #把x的值设为列表中的第一个元素，所以x有可能是列表中的任何一个值，从-3到3
        self.y = -3 #把y改成-3，让小球飞的快一些
        '''让小球来回反弹，增加三行代码，self=0给对象变量x赋值为0，个对象变量Y赋值为-1
        #self.x = 0
        #self.y = -1'''
        self.canvas_height = self.canvas.winfo_height() #保存画布的高度，防止小球从上下消失
        self.canvas_width = self.canvas.winfo_width()   #保存画布的快读，防止小球不会从两边消失
        self.hit_button = False #增加一个hit_button变量

    #判断小球是否击中球拍
    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id) #得到拍子的坐标并把它放到paddle_pos中

        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]: #小球的右侧大于球拍的左侧并且小左的左侧小于球拍的右侧
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]: #小球的底部pos[3]是否在糗百的顶部paddle_pos[1]且底部paddle_pos[3]之间
                return True
        return False

    def draw(self):
        '''让小球移动，id圆形的id，0表示不要水平移动，-1指屏幕上向上移动1个像素，小球会向上移动并消失
        #self.canvas.move(self.id,0,-1)'''

        #让小球来回反弹
        self.canvas.move(self.id,self.x,self.y) #对画布上move函数的调用改为传入变量x,y
        pos = self.canvas.coords(self.id)    #创建变量pos，赋值为画布函数coords，这个函数通过id来返回画布上任何画好的东西和当前的x,y坐标,可打印print(self.canvas.coords(self.id))
        '''#判断y1坐标（小球顶部）是否小于等于0，如果是，把变量设置为1，这样小球撞到屏幕的顶部将不再继续从纵坐标-1，实现不再向上移动
        #if pos[1] <= 0:
        #   self.y = 1
        #判断y2坐标（小球底部）是否大于于等于画布的高度canvas_height，如果是，把变量设置为-1，这样小球撞到屏幕的底部将不再继续从纵坐标-1，实现不再向下移动
        #if pos[3] >= self.canvas_height:
        #   self.y = -1'''
        if pos[1] <= 0: #使用新的对象变量来判断小球是否撞到画布的顶部或底部
            self.y = 3
        if pos[3] >= self.canvas_height:    #判断小球是否撞到屏幕底部，即判断它是否大于或定于canvas_height
            #判断小球是否撞到底部,一旦到底，则不再弹回
            self.hit_button = True
            #self.y = -3
        if self.hit_paddle(pos) == True:
            self.y = -3
        #使用新的对象变量来判断小球是否撞到画布的左侧或右侧
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3