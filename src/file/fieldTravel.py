__author__ = 'Administrator'


import os

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