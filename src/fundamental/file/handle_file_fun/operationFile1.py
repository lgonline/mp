__author__ = 'Administrator'

uinputs = input("would you download it? 1: yes, 2: no ")

if uinputs == '1':
    #filepath = input("Please input your local address : ")
    openfile = open('d:\\statistics.txt','w')
    print("download...")
    openfile.write('yesterday 25624 21301 19813')
    openfile.close()
    print("Download is finished!")
else:
    print("welcome to here again.")

openfile = open('d:\\statistics.txt')
context = openfile.read()
print(context)
openfile.close()