#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: 330mlcc 
@license: Apache Licence  
@contact: lg_online@126.com 
@site:  
@software: PyCharm 
@file: createEmail
@time: 18-5-16 下午11:51 
Description: 
"""

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

def make_mpa_msg():
    email = MIMEMultipart('alternative')
    text = MIMEText('Hello World!\r\n','plain')
    email.attach(text)
    html = MIMEText('<html><body><h1>Hello World!!!</h1></body></html>')
    email.attach(html)
    return email

def make_img_msg(fn):
    f = open(fn,'r')
    data = f.read()
    f.close()
    email = MIMEImage(data,name=fn)
    email.add_header('Content-Disposition','attachment;filename="%s"' % fn)
    return email

def sendMsg(fr,to,msg):
    s = SMTP('smtp-mail.outlook.com')
    errs = s.sendmail(fr,to,msg)
    s.quit()

if __name__ == '__main__':
    SENDER = 'mlcc330@hotmail.com'
    RECIPS = 'lg_online@126.com'

    print('Sending multipat alternative msg...')
    msg = make_mpa_msg()
    msg['From'] = SENDER
    msg['To'] = ','.join(RECIPS)
    msg['Subect'] = 'multipart alternative test'
    sendMsg(SENDER,RECIPS,msg.as_string())

    print('Sending image msg...')
    pass 
    
    