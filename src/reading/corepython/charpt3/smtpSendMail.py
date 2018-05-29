#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: 330mlcc 
@license: Apache Licence  
@contact: lg_online@126.com 
@site:  
@software: PyCharm 
@file: smtpSendMail
@time: 18-5-17 下午11:30 
Description: 
"""

from email.mime.text import MIMEText
import smtplib

#本段落为高级版本，解决邮件没有主题、收件人名字显示和提示不再收件人
from email import encoders
from email.header import Header
from email.utils import parseaddr,formataddr

def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

if __name__ == '__main__':


    # from_addr = input('From: ')
    # mail_passwd = input('password: ')
    # to_addr = input('To: ')
    # smtp_server = input("SMTP Server: ")
    from_addr = 'mlcc330@hotmail.com'
    mail_passwd = '#lgonline@HM&890*'
    to_addr = 'mlcc330@hotmail.com'
    smtp_server = 'smtp-mail.outlook.com'

    # msg = MIMEText('hello, send by python...', 'plain', 'utf-8')

    """
    服务器名称: smtp-mail.outlook.com
    端口: 587
    加密方法: STARTTLS
    """

    #本段落为高级版本，解决邮件没有主题、收件人名字显示和提示不再收件人
    msg = MIMEText('hello, send by python...','plain','utf-8')
    msg['From'] = _format_addr('Python爱好者<%s>' % from_addr)
    msg['To'] = _format_addr('管理员<%s>' % to_addr)
    msg['Subject'] = Header('来自SMTP的问候','utf-8').encode()

    server = smtplib.SMTP(smtp_server,587)
    server.set_debuglevel(1)                #打印出和SMTP服务器交互的所有信息
    server.starttls()
    server.login(from_addr,mail_passwd)     #登录SMTP服务器
    server.sendmail(from_addr,to_addr,msg.as_string())  #发邮件
    server.quit()
    pass 
    
    