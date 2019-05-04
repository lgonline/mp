#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
@author: mlcc
@file: classExtens.py
@time: 19-5-2 下午9:31 
Description: python中类的继承
"""

class ContactList(list):
    def search(self,name):
        matching_contacts = []

        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)

        return matching_contacts

class Contact:
    all_contacts = []
    # all_contacts = ContactList()

    # def __init__(self,name,email):
    #     self.name = name
    #     self.email = email
    #     Contact.all_contacts.append(self)

    def __init__(self,name='',email='',**kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        self.all_contacts.append(self)

#在子类中修改或替换父类的方法.不需要特殊的语法,子类中新创建的方法会自动调用
class Friend(Contact):
    def __init__(self,name,email,phone):
        # self.name = name
        # self.email = email
        #Contact中的name和email属性代码重复,使用super函数,返回父类实例化得到的对象.即,super获取父类对象的实例,然后调用__init__方法,传入参数
        super().__init__(name,email)
        self.phone = phone

if __name__ == '__main__':
    c1 = Contact("John A","johna@example.net")
    c2 = Contact("John B", "johnb@example.net")
    c3 = Contact("Jenna C", "jennac@example.net")

    print([c.name for c in Contact.all_contacts.search("John")])

    pass