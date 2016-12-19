#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = '330mlcc'

import socket
import sys,argparse,ntplib
from time import ctime
#自定义SNTP
import struct,time

#定义常量SEND_BUF_SIZE,RECV_BUF_SIZE,然后在一个函数中调用套接字实例的setsocket方法,用于修改套接字发送和接收缓冲区的大小
SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096

#获取本机信息
def print_machine_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print 'hostname is : ',hostname
    print 'ip address is : ',ip_address

#获取远程信息
def print_remote_machine_info():
    remote_host = 'www.jcloud.com'
    try:
        print remote_host,'remote ip address is : ',socket.gethostbyname(remote_host)
    except socket.error,err_msg:
        print '%s,%s',(remote_host,err_msg)

#使用底层网络函数，普通字符串形式的IP地址没有用，需要将它们转换成打包后的32位二进制格式
from binascii import hexlify

def convert_ipv4_adress():
    for ip_addr in ['127.0.0.1','192.168.47.1']:
        packed_ip_addr = socket.inet_aton(ip_addr)
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
        print 'IP Address : %s => Packed : %s, Unpacked ： %s' %(ip_addr,hexlify(packed_ip_addr),unpacked_ip_addr)

#通过指定的端口和协议找到服务名
def find_service_name():
    protocol_name = 'tcp'
    for port in [80,25,21]:
        print 'Port : %s => service name : %s ' %(port,socket.getservbyport(port,protocol_name))
    print 'Port : %s => service name : %s ' %(53,socket.getservbyport(53,'udp'))

#主机字节序和网络字节序之间的转换
# 转换底层网络应用时，获取需要处理通过电缆在两台设备之间传送的底层数据。在这种操作中，需要把主机操作系统发出的数据转换成网络格式或者做逆向转换
def convert_integer():
    data = 1234
    #32-bit,ntohl()把网络字节序转换成长整型主机自己序。函数名中的n表示网络，h表示主机，l表示长整型，s表示短整型，即16位
    print 'Original : %s => Long host byte order: %s, Network byte order: %s' %(data,socket.ntohl(data),socket.htonl(data))
    #16-bit
    print 'Original : %s => Short host byte order: %s, Network byte order: %s' % (data, socket.ntohs(data), socket.htons(data))

#设定并获取默认的套接字超时时间
#处理socket库某些属性的默认值，如套接字的超时时间
def test_socket_timeout():
    #创建套接字对象，第一个参数是地址族，第二个参数是套接字类型
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print 'Default socket timeout is : ',s.gettimeout()
    s.settimeout(100)
    print 'Current socket timeout is : ',s.gettimeout()

#处理套接字错误，解决常出现的一方由于挽留过或其它原因无法响应,需要加载sys和argparse
def handle_socket_error():
    #argpares模块把命令行参数传入脚本以及脚本中解析命令行参数
    parset = argparse.ArgumentParser(description='Socket Error Examples')
    #参各命令行参数：主机名、端口号、文件名
    parset.add_argument('--host',action='store',dest='host',required=False)
    parset.add_argument('--port',action='store',dest='port',type=int,required=False)
    parset.add_argument('--file',action='store',dest='file',required=False)
    given_args = parset.parse_args()
    host = given_args.host
    port = given_args.port
    filename = given_args.file

    #First try-except block --create socket
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except socket.error,e:
        print 'Error creating socket : %s ' % e
        sys.exit()

    #second try-except block --connect to given host/port
    try:
        s.connect((host,port))
    #gaierror处理地址相关的错误，除此之外，socket.herror处理CAPI抛出的异常，
    except socket.gaierror, e:
        print 'Address-relatd error connecting to server : %s' % e
        sys.exit(1)
    except socket.error,e:
        print 'Connection error : %s' % e
        sys.exit()

    #Third try-except bloc --sending data
    try:
        s.sendall('GET %s HTTP/1.0\r\n\r\n' % filename)
    except socket.error,e:
        print 'Error sending data : %s' %e

    while 1:
        #Fourth tr-except block --waiting to receive data from remote host
        try:
            buf = s.recv(2048)
        except socket.error,e:
            print 'Error receiving data : %s' % e
        if not len(buf):
            break
        #write the received data
        sys.stdout.write(buf)

#修改套接字发送和接收缓冲区的大小
def get_modify_buff_size():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #get the size of the socket's send buffer,getsockopt用于获取套接字对象的属性
    bufsize = sock.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
    print 'Buffer size [Before]:%d' %bufsize
    #setsockopt用于修改套接字对象的属性
    sock.setsockopt(socket.SOL_TCP,socket.TCP_NODELAY,1)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,SEND_BUF_SIZE)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,RECV_BUF_SIZE)

    bufsize = sock.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
    print 'Buffer size [After]:%d' %bufsize

#把套接字修改成阻塞或非阻塞模式，默认情况，TCP套接字是阻塞模式，即除非完成某操作，否则不会把控制权交给横须，如调用connect（）后，\r
# 连接操作会组织程序继续向下执行，直到链接成功为止，但不希望等待服务器响应时，应考虑取消该功能，这时需要修改为非阻塞模式
#setblock(1)为阻塞模式，setblock(0)为非阻塞模式
def change_tcp_parttner():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setblocking(1)
    s.settimeout(0.5)
    s.bind(('127.0.0.1',0))

    socket_address = s.getsockname()
    print "Trivial Server launched on socket: %s" %str(socket_address)
    while(1):
        s.listen(1)

#重用套接字地址，有时需要在同一个端口上运行套接字服务器，如果客户端需要一直连接指定的端口，就很有用
#建立套接字后，查询地址重用的状态，调用setsocket方法，修改重用状态的值，在按照常规步骤，把套接字绑定到一个地址监听客户端连接
#在终端运行代码，在另一个终端telnet localhost 8282，关闭服务器后仍可以使用同一个端口再次连接，但把SO_REUSEADDR注销，服务器将不会再次运行脚本
def reuse_socket_addr():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #get the old state of the so_requseaddr option
    old_state = sock.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
    print 'Old sock state is : %s' %old_state
    #enable the so_reuseadr option
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    new_state = sock.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
    print 'New sock state is : %s' %new_state

    local_port = 8282

    srv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    srv.bind('',local_port)
    srv.listen(1)
    print 'Listening on port : %s' %local_port

    while True:
        try:
            connection, addr = srv.accept()
            print 'Connected by %s:%s' %(addr[0],addr[1])
        except KeyboardInterrupt:
            break
        except socket.error, msg:
            print '%s' %(msg)

#从NTP获取并打印当前时间，需要ntplib
def get_time_from_ntpserver():
    ntp_client = ntplib.NTPClient()
    response = ntp_client.request('pool.ntp.org')
    print ctime(response.tx_time)

#自定义的SNTP客户端
NTP_SERVER = '0.uk.pool.ntp.org'
TIME1970 = 2208988800L
def sntp_client():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    data = '\x1b' + 47 * '\0'
    client.sendto(data,(NTP_SERVER,123))
    data, address = client.recvfrom(1024)
    if data:
        print 'Response received from : ',address
    t = struct.unpack('!12I',data)[10]
    t -= TIME1970
    print '\tTime=%s' % time.ctime(t)


if __name__ == '__main__':
    #print_machine_info()
    #print '********************************'
    #print_remote_machine_info()
    ##print '********************************'
    #convert_ipv4_adress()
    #print '********************************'
    #find_service_name()
    #print '********************************'
    #convert_integer()
    #print '********************************'
    #handle_socket_error()
    #print '********************************'
    #get_modify_buff_size()

    #change_tcp_parttner()

    #reuse_socket_addr()

    #get_time_from_ntpserver()

    sntp_client()