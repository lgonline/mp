__author__ = 'Administrator'

from obj.Apple import Fruit

if __name__ == "main":
    apple = Fruit(hasNotHarvest,setColor('green'))
    print(apple.hasHarvest,apple.color)
    apple.config(hasHarvest,setColor('red'),canNotEat)
    print(apple.hasHarvest,apple.color,apple.eat)
    apple.config(hasHarvest,setColor('red'),canNotEat)