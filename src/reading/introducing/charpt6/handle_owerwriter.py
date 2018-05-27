#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: lgonline 
@license: Apache Licence  
@contact: lgonline@hotmail.com 
@site:  
@software: PyCharm 
@file: handle_owerwriter.py 
@time: 11/7/17 11:30 PM 
"""

class Quote():
    def __init__(self,person,words):
        self.person = person
        self.words = words

    def who(self):
        return self.person

    def says(self):
        return self.words+'.'

class QuestionQuote(Quote):
    def says(self):
        return self.words+'?'

class ExclamationQuote(Quote):
    def says(self):
        return self.words+'!'

if __name__ == "__main__":
    quote = Quote('Elmer Fudd','I"m hunting wabbits')
    print(quote.who(),' says : ',quote.says())

    quote1 = QuestionQuote('BUgs Fudd', 'What"s up, doc')
    print(quote1.who(), ' says : ', quote1.says())

    quote2 = ExclamationQuote('Daffy Duck', 'It"s rabbit season')
    print(quote2.who(), ' says : ', quote2.says())

    print '************************************************'

    def who_says(obj):
        print(obj.who(),' says ',obj.says())

    who_says(quote)
    who_says(quote1)
    who_says(quote2)