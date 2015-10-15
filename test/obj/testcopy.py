#/usr/bin/python
__author__ = 'hcm'

import copy

class Car:
    pass

if __name__ == "__main__":
    toyota = Car()
    toyota.wheels = 4

    honda = Car()
    honda.wheels = 3

    print('the init parameter of toyota.wheels is : ', toyota.wheels)
    print('the init parameter of honda.wheels is : ', honda.wheels)

    nissan = copy.copy(toyota)
    nissan.wheels = 6
    print('the old parameter of toyota.wheels is : ',toyota.wheels)
    print('the old parameter of nissan.wheels is : ',nissan.wheels)