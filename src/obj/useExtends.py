__author__ = 'Administrator'

class Fruit:
    def __init__(self,color):
        self.color = color
        print("The fruit color is : ",color)

    def grow(self):
        print("grow...")

class Apple(Fruit):
    def __init__(self,color):
        Fruit.__init__(self,color)
        print("Apple's color is : ",color)

class Banana(Fruit):
    def __init__(self,color):
        Fruit.__init__(self,color)
        print("Banana's color is : ",color)

    def grow(self):
        print("Banana is growing...")

if __name__ == "__main__":
    apple = Apple("Red")
    apple.grow()
    banana = Banana("Yellow")
    banana.grow()