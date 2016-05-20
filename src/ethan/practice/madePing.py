__author__ = 'Administrator'

def ippool(ip):
    list = []
    for i in range(1,255):
        list.append('%s.%d' % (ip,i))
    return list