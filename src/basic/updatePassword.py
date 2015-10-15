__author__ = 'Administrator'

def updatePassword():
    i = 1
    while i <= 1:
        oldPassword = input("Please input your old password : ")
        if(oldPassword != "python"):
            print("The init password is incorrect, please input it again.")
        else:
            newPassword = input("Please input your new password : ")
            if(len(newPassword) > 6) and (len(newPassword) < 18):
                renewPassword = input("Please input your new password again : ")
                if(renewPassword != newPassword):
                    print("the twice input is inconsistent.")
                else:
                    print("Congratulation, update password is successful.")
                    break
            else:
                print("your password can not more less 6 bit or more than 20 bit.")
                continue
    else:
        print()