#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
@author: mlcc
@file: classExtens.py
@time: 19-5-2 下午9:31 
Description: real estate management system
"""

class RealestateProperty:
    # 因需要用于多重继承,添加了**kwargs参数
    def __init__(self,square_feet='',beds='',baths='',**kwargs):
        # 调用super().__init__,防止它不是在继承链的最后一层被调用
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def dispalay(self):
        print("REAL ESTATE MGMT SYSTEM PROPERTY DETAILS")
        print("========================================")
        print("squeare footage : {}".format(self.square_feet))
        print("bedrooms : {}".format(self.num_bedrooms))
        print("baths : {}".format(self.num_baths))
        print()

    def prompt_init(self):
        return dict(square_feet=input("Enter the square feet : "),
                    beds=input("Enter number of bedrooms : "),
                    baths=input("Enter number of baths : "))

    prompt_init = staticmethod(prompt_init)

class Apartment(RealestateProperty):
    valid_laundries = ("coin","ensuite","none")    # laundries 洗衣店 ensuite 套房 coin 硬币   valid 有效的
    valid_balconies = ("yes","no","solarium")       # balconies 阳台  solarium 日光浴室

    def __init__(self,balcony='',laundry='',**kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().dispalay()
        print("APARTMENT DETAILS")
        print("balcony : %s " % self.balcony)
        print("laundry : %s " % self.laundry)

    def prompt_init(self):
        parent_init = RealestateProperty.prompt_init()
        laundry = ''
        while laundry.lower() not in Apartment.valid_laundries:
            lanundry = input("What laundry facilities does th eproperty have?({})".format(", ".join(Apartment.valid_laundries)))

        balcony = ''
        while balcony.lower() not in Apartment.valid_balconies:
            balcony = input("Does the  property have a balcony?({})".format(", ".join(Apartment.valid_balconies)))

        parent_init.update({
            "laundry": laundry,
            "balcony": balcony,
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)

class House(RealestateProperty):
    valid_garage = ("attached","detached","none")   # detached 独立的 attached 附属的 garage 车库
    valid_fenced = ("yes","no")                     # fenced 围栏

    def __init__(self, num_stories='',garage='',fenced='',**kwargs):
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def dispalay(self):
        super().dispalay()
        print("HOUSE DETAILS")
        print("# of stories : {}".format(self.num_stories))
        print("garage : {}".format(self.garage))
        print("fenced yard : {}".format(self.fenced))

    def prompt_init():


