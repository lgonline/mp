__author__ = 'Administrator'

while 1 == 1:
    theOne = int(input("please input that your first numbers :"))
    theSecond = int(input("please input that your second numbers :"))
    symbol = input("please input your want method : ")

    if symbol == "+":
        print(theOne,"+",theSecond,"=",theOne+theSecond)
    elif symbol == '-':
        print(theOne,"-",theSecond,"=",theOne-theSecond)
    elif symbol == '*':
        print(theOne,"*",theSecond,"=",theOne*theSecond)
    elif symbol == '/':
        if theSecond == 0:
            print("your second number input is not zero")
        else:
            print(theOne,"/",theSecond,"=",theOne/theSecond)

    print("Do your want calculate?")
    operation = input("")
    if operation == 'y':
        continue
    else:
        break
else:
    print("the programe is exist!")