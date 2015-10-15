__author__ = 'Administrator'

#using default parameter to check users
def checkLogin(username,password):
    if (username == "admin") and (password == "admin"):
        print("congratulations, your are login is successful!")
    else:
        print("login failed!")

#using list parameter to check users
def checkLoginUseList(* userpwd):
    username = userpwd[0]
    password = userpwd[1]
    if(username == "admin") and (password == "admin"):
        print("congratulations, your are login is successful!")
    else:
        print("login failed!")

#using dictionary parameter to check users
def checkLoginUseDictionary(** userpwd):
    keys = userpwd.keys()
    username=''
    password=''
    for key in keys:
        if 'username' == key:
            username=userpwd[key]
        if 'password' ==key:
            password=userpwd[key]

    if(username=="admin") and (password=="admin"):
        print("congratulations, your are login is successful!")
    else:
        print("login failed!")