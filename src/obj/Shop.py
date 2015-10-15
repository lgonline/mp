__author__ = 'Administrator'

def abstract():
    raise NotImplementedError("Sorry, prohibit implement the supper class")

class ClothStore:
    def __init__(self):
        self.brand = "Lenovo"
        print("The brand is ",self.brand)
        if self.__class__ is ClothStore:
            abstract()

class GrilClothStore(ClothStore):
    def __init__(self):
        self.brand = "HP"
        print("The brand is : ",self.brand)

class BoyClothStore(ClothStore):
    def __init__(self):
        self.brand = "ACER"
        print("The brand is : ",self.brand)

class BoyCloth(BoyClothStore,ClothStore):
    def __init__(self,name,make,price,wash):
        print("The global brand is ",ClothStore.__init__(self))
        print("The local brand is ",BoyClothStore.__init__(self))
        self.name = name
        self.make = make
        self.price = price
        self.wash = wash

    def showInfo(self):
        print("The name is ",self.name,", make is ",self.make,"price is ",self.price,"and the wash is ",self.wash)