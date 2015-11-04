__author__ = 'Administrator'

import os
import shutil
print("---------------welcome to use mynotes-------------")
conn = True

while conn:
    operation = int(input("would you input your selection.\n 1. Write\n 2.Review\n 3.Remove\n 4. Backup\n5. Recovery\n6.Quit\n"))
    if operation == 1:
        openfile = open("d:\\mynote.txt","a+")
        context = input("please input your wanted:\n")
        openfile.write(context)
        print("----------------")
    elif operation == 2:
        print("The context as follow:\n")
        openfile = open("d:\\mynote.txt","a+")
        readfile = openfile.readlines()
        for context in readfile:
            print(context)
        openfile.close()
        print("----------------------")
    elif operation == 3:
        confirmremove = int(input("Would you want to format the note? \n1. yes \n2. no\n"))
        if confirmremove == 1:
            print("The note is formating...")
            if os.path.exists("d:\\mynote.txt"):
                os.remove("d:\\mynote.txt")
                print("format notepad is successful!")
                open("d:\\mynote.txt","a+")
            else:
                print("the notepad is existing your wanted")
        elif confirmremove == 2:
            break
        else:
            break
    elif operation == 4:
        backupfile = int(input("would you want to backup the notepad \n1. yes\n2. no\n"))
        if backupfile == 1:
            print("The notepad is backuping...")
            shutil.copyfile("d:\\mynote.txt","d:\\mynote_backup.txt")
            print("the file backup is successful!")
        elif backupfile == 2:
            break
        else:
            break
    elif operation == 5:
        recoverfile = int(input("Would you want to recovery th enotepad.\n1. yes\n2. no\n"))
        if recoverfile == 1:
            print("The notepad is recoverying...")
            shutil.copyfile("d:\\mynote_backup.txt","d:\\mynote.txt")
            print("The recovery is successful!")
        elif recoverfile == 2:
            break
        else:
            break
    else:
        print("bye")
        conn = False