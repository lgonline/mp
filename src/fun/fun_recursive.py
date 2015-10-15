__author__ = 'Administrator'

def  myrecursive(n):
    if n == 1:
        return 1
    return n * myrecursive(n - 1)

#advanced function of recursive
def fact(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num == 1:
        return product
    return fact_iter(num-1,num * product)

if __name__ == "__main__":
    sum = myrecursive(5)
    print(sum)

    sum1 = fact_iter(5,1)
    print(sum1)
