__author__ = 'Administrator'

def calc(*numbers):
   # nums = map(int, numbers)
    sum = 0
    for n in numbers:
        sum  = sum +int(n)

    return sum

if __name__ == "__main__":
    inputs = input('aaaa : ')
    input = inputs.split(',')
    for i in input:
        print(type(i))
    print(calc(*input))
    #sum = calc(1,2,3,4,5)
   # print(sum)