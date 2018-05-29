__author__ = 'Administrator'

from obj import Shop

shops = Shop.BoyCloth("liugang", "gaungzhou", 1500, "china")
shops.showInfo()

if issubclass(Shop.BoyCloth, Shop.BoyClothStore) == True:
    print("The class BoyCloth is a subclass of BoyClothStore")
else:
    print("The class BoyCloth is not a subclass of BoyClothStore")

if isinstance(shops, Shop.ClothStore) == True:
    print("The class BoyCloth is a instance of BoyClothStore")
else:
    print("The class BoyCloth is not a instance of BoyClothStore")