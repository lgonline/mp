#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = 'liugang5'


class Account(object):
    num_accounts = 0

    def __init__(self,name,blance):
        self.name = name
        self.blance = blance
        Account.num_accounts += 1

    def __del__(self):
        Account.num_accounts -= 1

    def deposit(self,amt):
        self.blance = self.blance + amt

    def withdraw(self,amt):
        self.blance = self.blance - amt

    def inquirey(self):
        return self.blance


if __name__ == "__main__":
    usera  = Account("liguang",1000)
    '''
    print("usera.__init__() is ",usera.__init__()," usera.__del__() is ",usera.__del__(),
            " usera.deposit() is ",usera.deposit()," usera.withdraw() is ",usera.withdraw(),
            "usera.inquirey() is ",usera.inquirey())
    '''
    print(usera.name)
    #usera.__del__()
    usera.withdraw(100)
    print(usera.blance)