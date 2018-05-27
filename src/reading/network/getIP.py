__author__ = 'Administrator'

import socket

#get local ip
localIP = socket.gethostbyname(socket.gethostname())
myname = socket.getfqdn(socket.gethostname())
myaddr = socket.gethostbyname(myname)
print('local ip : ',localIP)
print('myname is : ',myname)
print('my ip is : ',myaddr)

#get public ip
#import re,urllib
#from subprocess import Popen,PIPE
#print('my machine private ip addr is : ',re.search('\d+.\d+.\d+.\d+',Popen('ipconfig',stdout=PIPE).stdout.read()).group(0))
#print('my machine public ip addr is : '+re.search('\d+.\d+.\d+.\d+',urllib.request.urlopen("http://www.ip138.com").read()).group(0))