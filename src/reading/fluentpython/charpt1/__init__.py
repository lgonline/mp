#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = '330mlcc'

import random

def guessNumber():
    print "I am thinking of a number between 1 and 20"
    print "Take a guess"

    guessMaxNumber = 0
    guessMinNumber = 0
    countNumer = 0

    while True:
        myrandom = random.randint(1, 20)
        #print myrandom
        if myrandom < 16:
            #print "Your guess is too low, Take a guess again."
            guessMinNumber += 1
            #print guessnumber
            continue
        elif myrandom > 16:
            #print "Your guess is too high, Take a guess again."
            guessMaxNumber += 1
            continue
        elif myrandom == 16:
            countNumer = guessMaxNumber + guessMinNumber
            print "Good job! You guessed my number in %d times." %(countNumer)
            print "max is : ",guessMaxNumber," times and min is ",guessMinNumber," times."
            break
        else:
            print "None."
            break

if __name__ == '__main__':
    guessNumber()
    pass

