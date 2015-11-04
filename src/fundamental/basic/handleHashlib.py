__author__ = 'Administrator'

import hashlib

src = 'this is a md5 test.'
m2 = hashlib.md5()
m2.update(src)
print(m2.hexdigest())

md5 = hashlib.md5()
#md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
md5.update(str.encode('utf-8'))
print(md5.hexdigest())

md5.update(str.encode('utf-8'))
print(md5.hexdigest())

'''
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
#print(md5.hexdigest())
'''
'''
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9',
    '123456':'e10adc3949ba59abbe56e057f20f883e',
    '888888':'b70c83d512609ce9e35b3eede636309e',
    'password':'5f4dcc3b5aa765d61d8327deb882cf99'
}
'''
'''
inputs = input('Please enter your password.\n')
#print(type(inputs))
print('your inputs is : ',inputs)
def calcmd5(inputs):
    md5.update(inputs)
    return md5.hexdigest()

print("md5 values is : ",calcmd5(inputs))

print('---------------------------------------------------')
#print('your inputs is : ',inputs)
#md5.update(inputs.encode('utf-8'))
#print(inputs,' md5.hexdigest() is : ',md5.hexdigest())

#print(hashlib.md5(inputs))
'''