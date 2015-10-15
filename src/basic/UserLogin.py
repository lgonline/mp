__author__ = 'Administrator'

db = {}

def newuser():
    prompt = "please input your account, thanks."
    while True:
        username = input(prompt)
        if username in db:
            prompt = "your account was registered, please use another to register it"
            continue
        else:
            password = input("Please input your password for register : ")
            db[username] = password
            break

def oldUser ():
    username = input("Please input your login account : ")
    password = input("Please input your login password : ")
    userpwd = db.get(username)
    if userpwd == password:
        print("welcome ",username," , access this web site.")
    else:
        print("your username or password is failed , so you cannot login this web site.")

def showmeun ():
    prompt = "Please input your status: [ n : register e : login]"
    conn = False
    while not conn:
        chosen  = False
        while not chosen:
            try:
                choice = input(prompt).strip()[0].lower()
            except(EOFError,KeyboardInterrupt):
                choice = 'q'
            print("you selection is : ",choice)
            if choice not in 'neq':
                print("your input is unlawful, please re-input again.")
            else:
                chosen = True
                conn = True

            if choice == 'n':
                newuser()
            elif choice == 'e':
                oldUser()
            else:
                showmeun()
            showmeun()