#!/usr/bin/python
__author__ = 'ethan'



if __name__ == "__main__":
    target = 60

    while True:
        value = input("enter an integer between 1 and 100. \n")
        try:
            value = int(value)
            break
        except ValueError:
            print('i said enter an integer!')

    if value > target:
        print(value," is too high")
    elif value < target:
        print(value, ' is too low')
    else:
        print('pefect')