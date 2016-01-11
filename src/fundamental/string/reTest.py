__author__ = 'Administrator'
import re
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print('m.group is : ',m.group())
print('m.group(1) is : ',m.group(1))
print('m.group(2) is : ',m.group(2))

t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print('m.group() is : ',m.group())
print('m.group(1) is : ',m.group(1))
print('m.group(2) is : ',m.group(2))
print('m.group(3) is : ',m.group(3))

#mail1 = 'someone@gmail.com'
#re_emails = re.match(r'[a-zA-Z0-9\.\ ]+@[a-zA-Z0-9\.\ ]+\.[a-zA-Z0-9\.\ ]+',mail1)
re_Email = re.compile(r'[a-zA-Z0-9\.\_]+@[a-zA-Z0-9\.\_]+\.[a-zA-Z0-9\.\_]+')
re_GroupEmail = re.compile(r'(<+?[a-zA-Z\s]+>+?)\s*([a-zA-Z0-9\.\_]+@[a-zA-Z0-9\.\_]+\.[a-zA-Z0-9\.\_]+)')

def mactchEmail(email):
    return re_Email.match(email)

def getMatchName(email):
    return re_GroupEmail.match(email).group()

print(mactchEmail('someone@gmail.com'))
print(mactchEmail('bill.gates@microsoft.com'))
print(getMatchName('<Tom Paris> tom@voyager.org'))
#print(re_emails.group())