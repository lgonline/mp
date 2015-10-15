__author__ = 'Administrator'

def checkUserInput(username,age,phone):
    username = input("Please input your name : ")
    age = int(input("Please input your age : "))
    phone = int(input("Please input your phone : "))

    if(len(username) < 3):
        print("sorry, your input character can not more less 3 bit")
    elif(len(username) > 20 ):
        print("sorry, your input character can not more than 20 bit")
    else:
        print(username)

    if age < 18:
        print("sorry, younger, you can not register this web site")
    elif age > 60:
        print("sorry, senior,may be you can not register this web site")
    else:
        print("welcome to register this web site.")

    if phone < 18:
        print("sorry, younger, you can not register this web site")
    elif phone > 60:
        print("sorry, senior,may be you can not register this web site")
    else:
        print("welcome to register this web site.")