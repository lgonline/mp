__author__ = 'Administrator'

def checkPID(pid):
    if len(pid) == 18:
        print("your pid is : "+pid)
    else:
        print("your pid length is incorrect")

    ID_add = pid[0:6]
    ID_birth = pid[6:14]
    ID_sex = pid[14:17]
    ID_check = pid[17]

    #ID_add是身份证中的区域代码，如果有一个行政区划代码字典，就可以用获取大致地址#

    year = ID_birth[0:4]
    moon = ID_birth[4:6]
    day = ID_birth[6:8]
    print("Birthday: ",year+'-'+moon+'-'+day)

    if int(ID_sex) % 2 == 0:
        print('Gender : Female')
    else:
        print('Gender : Male')

if __name__ == '__main__':
    while True:
        PID=input('Please input your pid. \n ')
        checkPID(PID)
        if PID == 'q':
            break