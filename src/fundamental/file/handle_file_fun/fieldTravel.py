__author__ = 'Administrator'


import os

def haneldOSPath():
    print('os.path.abspath(__file__) is : ', os.path.abspath(__file__))
    print('os.path.abspath(".") is : ', os.path.abspath('.'))
    print(os.listdir(os.path.abspath('.')))
    print(os.path.isdir(os.path.abspath('.')))
    print(os.path.exists(os.path.abspath('.')))

def createFileDemo():
    filepath = input("Please input your file path : ")
    filename = input("Please input your file name : ")
    file = filepath + ":\\\\" + filename + ".txt"
    print(file)
    if os.path.isfile(file):
        print("file is existing")
    else:
        f = open(file, mode="w", encoding="UTF-8")
        print("file", file, " has been created.")

def handleFilePath():
    flag = True

    while flag:
        filepath = input("Please input your file path : \n")
        if (filepath == 'c') or (filepath == 'd'):
            filename = input("Please input your file name : \n")
        else:
            print("your input file path is incorrect.")
        file = filepath + ":\\\\" + filename + ".txt"
        if os.path.isfile(file):
            print("file is existing")
        else:
            myfile = open(file, mode="w", encoding="UTF-8")

        content = input("please input you wanted.\n")
        myfile = open(file, "a+")
        myfile.write(content)

        openfile = open(file)
        filecontent = openfile.readlines()
        for line in filecontent:
            print(line)

        operation = int(input("do you want next step?\n 1.yes\n2. no\n"))
        if operation == 1:
            continue
        elif operation == 2:
            print("the project is quit.")
            flag = False
        else:
            break

def visitDir(path, lists = []):
    filedir = os.listdir(path)
    for dir in filedir:
        pathname = os.path.join(path,dir)
        if not os.path.isfile(pathname):
            visitDir(pathname, lists)
        else:
            #print(pathname)
            lists.append(pathname)
    return lists


if __name__ == "__main__":
    path = r"D:\apache-tomcat-7.0.59"
    #visitDir(path)
    filepath = input("Please the file path to save your wanted.")
    filename = input("please the file name to save your wanted.")
    file = filepath+":\\\\"+filename+".txt"
    if os.path.isfile(file):
        print("the file name is existing")
    else:
        openfile = open(file,mode="w",encoding="utf-8")

    openfile = open(file,"a+")
    content = visitDir(path)
    #print(content)
    str = ('').join(content)
    openfile.write(str)
    openfile.close()