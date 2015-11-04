__author__ = 'Administrator'

import math

def move(n,a,b,c):
    if n <= 0:
        print('The parameter is not incorrect')
    else:
        if n ==1:
            print('move',a,'--->',c)
            return
        else:
            move(n-1,a,c,b)
            move(1,a,b,c)
            move(n-1,b,a,c)

if __name__ == "__main__":
    n = int(input('please the numbers of flow.'))
    print('The total steps is : ',(int(math.pow(2,n)-1)))
    move(n,'A','B','C')