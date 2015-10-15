__author__ = 'Administrator'

#stringio, read or write str type data in memory
from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('World!!!')
print('string io demo, the f.getValue() is ',f.getvalue())

#byteio, read or write byte type data in memory
from io import BytesIO
fb = BytesIO()
fb.write("中文".encode('utf-8'))
#the data was writed by encode of utf-8, is not str type
print('fb.getvalue() is : ',fb.getvalue())