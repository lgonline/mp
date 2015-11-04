__author__ = 'Administrator'

items=['dcy','admin','mxl','another','happy','sorry']
i=1
while i<=1:
    i+=1
    print("---------starting-------")
    for danqu in items:
        if danqu == 'sorry':
            break
        if danqu == 'admin':
            continue

        print(" the ",i-1,' times to show the name is ; ',danqu)