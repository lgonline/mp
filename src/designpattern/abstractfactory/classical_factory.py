#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

'''
为了演示抽象工厂模式，我们来写一段程序，用以生成简单的“示意图”（diagram）。
这段程序会用到两个“工厂”（factory）：一个用来生成纯文本格式的示意图，另一个用来
生成SVG（Scalable Vector Graphics，可缩放的矢量图）格式的示意图。
'''

class Diagram:
    def add(self,component):
        for y, row in enumerate(component.rows):
            for x, char in enumerate(row):
                self.diagram[y + component.y][x + component.x] = char

class Text:
    def __init__(self,x,y,text,fontsize):
        self.x = x
        self.y = y
        self.rows = [list(text)]

class DiagramFactory:
    def make_diagram(self,width,height):
        return Diagram()

class SvgDiagram:
    def add(self,component):
        self.diagram.append(component.svg)

class SvgDiagramFactory(DiagramFactory):
    def make_digram(self,width,height):
        return SvgDiagram(width,height)

    def make_rectangle(self,x,y,width,height,file="white",stroke="black"):
        return Rectangle(x,y,width,height,fill,stroke)

    def make_text(self,x,y,text,fontsize=12):
        return Text(x,y,text,fontsize)

class DiagramFactory:
    def make_diagram(self,width,height):
        return Diagram(width,height)

    def make_rectangle(self,x,y,width,height,file="white",stroke="black"):
        return Rectangle(x,y,width,height,fill,stroke)

    def make_text(self,x,y,text,fontsize=12):
        return Text(x,y,text,fontsize)

#create_diagram 函数只有一个参数，就是绘图所用的工厂，该函数用这个工厂创建出所需的示意图。
#  此函数并不知道工厂的具体类型，也无须关心这一点，它只需要知道工厂对象具备创建示意图所需的接口即可。
def create_diagram(factory):
    diagram = factory.make_diggram(30,7)
    rectangle = factory.make_rectangle(4,1,22,5,"Yellow")
    text = factory.make_text(7,3,"Abstract Factory")
    diagram.add(rectangle)
    diagram.add(text)
    return diagram

if __name__ == "__main__":
    txtDiagram = create_diagram(DiagramFactory())
    txtDiagram.save(textFilename)

    svgDiagram = create_diagram(SvgDiagramFactory())
    svgDiagram.save(svgFilename)
    pass