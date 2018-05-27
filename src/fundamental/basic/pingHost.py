__author__ = 'Administrator'

#!/usr/bin/env python
#coding:utf-8
import os,time,random,sys#,threadpool,sys
#from progressbar import *

COUNT=0
tit=1000
PINGIP=[]

def main():
    ipd=None
    if len(sys.argv)==2:
        ipd=sys.argv[1]

    a=os.popen("ipconfig").read()
    s=a.split('.')
    del s[-1]
    ips='.'.join(s)
    ipl=""
    if ipd==None:
        ipl=ips
    else:
        ipl=ipd
    print("搜索网段:"+ipl)
    List=myIpPool(ipl)
    #pool=threadpool.ThreadPool(100)
    #req=threadpool.makeRequests(ping,List,print_result)
    #for r in req:
    #    pool.putRequest(r)
    #pool.wait()
    #print()
    print(PINGIP)

def myIpPool(ipPrefix):
    List=[]
    for i in range(1,255):
        List.append("%s.%d" %(ipPrefix,i))
    return List

def print_result(request, result):
    global COUNT
    global PINGIP
    global pbar
    COUNT+=1
    List=[]
    if result!=None:
        #print "the result is %s %r" % (request.requestID, result)
        PINGIP.append(result)
    aa=int(COUNT/256.00*100)

    #print(COUNT,aa)
    pbar.update(aa)

def ping(ip):
    #print("ip:"+ip)
    ret=os.popen("ping -c 2 -W 2 "+ip).readlines()
    bak="|".join(ret)
    pp="min/avg/max/stddev" #匹配结果,不同操作系统可能不一样
    '''
    print("长度:"+str(len(ret)))
    print(bak)
    print(bak.find(pp))
        '''
    if(bak.find(pp)!=-1):
        return ip

if __name__=='__main__':
    #pbar = ProgressBar().start()
    main()
    input = input('please input the ip address you wanted.\n')
    ping(input)