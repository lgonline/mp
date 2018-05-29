#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: 330mlcc 
@license: Apache Licence  
@contact: lg_online@126.com 
@site:  
@software: PyCharm 
@file: pop3GetMail
@time: 18-5-18 上午12:04 
Description: 
"""

import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr



if __name__ == '__main__':
    email = 'mlcc330@hotmail.com'
    mail_passwd = '#lgonline@HM&890*'
    # to_addr = 'mlcc330@hotmail.com'
    pop3_server = 'pop-mail.outlook.com'

    def guess_charset(msg):
        charset = msg.get_charset()
        if charset is None:
            content_type = msg.get('Content-Type', '').lower()
            pos = content_type.find('charset=')
            if pos > 0:
                charset = content_type[pos + 8:].strip()

        return charset


    def decode_str(s):
        value, charset = decode_header(s)[0]
        if charset:
            value = value.decode(charset)
        return value


    def print_info(msg, indent=0):
        if indent == 0:
            for header in ['From', 'To', 'Subject']:
                value = msg.get(header, '')
                if value:
                    if header == 'Subject':
                        value = decode_str(value)
                    else:
                        hdr, addr = parseaddr(value)
                        name = decode_header(hdr)
                        value = u'%s <%s>' % (name, addr)
                print('%s%s: %s' % (' ' * indent, header, value))

        if (msg.is_multipart()):
            parts = msg.get_payload()
            for n, part in enumerate(parts):
                print('%spart %s' % (' ' * indent, n))
                print('%s-----------------' % (' ' * indent))
                print_info(part, indent + 1)
        else:
            content_type = msg.get_content_type()
            if content_type == 'text/plain' or content_type == 'text/html':
                content = msg.get_payload(decode=True)
                charset = guess_charset(msg)
                if charset:
                    content = content.decode(charset)
                print('%sText: %s' % (' ' * indent, content + '...'))
            else:
                print('%sAttachment: %s' % (' ' * indent, content_type))



    server = poplib.POP3(pop3_server,port=995)               # 连接到POP3服务器:
    server.set_debuglevel(1)                            # 可以打开或关闭调试信息:
    print(server.getwelcome().decode('utf-8'))          # 可选:打印POP3服务器的欢迎文字:

    # 身份认证:
    server.user(email)
    server.pass_(mail_passwd)

    print('Messages:%s. Size:%s' % server.stat())       # stat()返回邮件数量和占用空间:
    resp,mails,octets = server.list()                   # list()返回所有邮件的编号:
    print(mails)                                        # 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]

    index = len(mails)                                  # 获取最新一封邮件, 注意索引号从1开始:
    resp,lines,octets = server.retr(index)              # list()返回所有邮件的编号:

    msg_content = b'\r\n'.join(lines).decode('utf-8')   # lines存储了邮件的原始文本的每一行,可以获得整个邮件的原始文本:
    msg = Parser().parsestr(msg_content)                # 稍后解析出邮件:
    print_info(msg)
    server.quit()

    """
    服务器名称: pop-mail.outlook.com
    端口: 995
    加密方法: TLS
    """

    pass 
    
    