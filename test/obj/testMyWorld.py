__author__ = 'Administrator'

from obj import MyWorld

if __name__ == "__main__":
    mystr = input("please input your object (person, pig, rooster) : ")
    myworld = MyWorld()

    if mystr == "person":
        myworld.person()
    elif mystr == "pig":
        myworld.pig()
    elif mystr == "rooster":
        myworld.rooster()
    else:
        print("sorry, no class your inputed")