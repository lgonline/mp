__author__ = 'Administrator'

import urllib
from urllib import parse

name = 'lgonline'
num = 6
baseurl = 'http://www.baidu.com/~dcy'
final = baseurl+"?name="+name+"&num="+str(num)

print("No use the function of quote : ",final)
print("Use the function of quote : ",urllib.parse.quote(final))
print("Use the function of quote_plus : ",urllib.parse.quote_plus(final))

encodingurl = urllib.parse.quote_plus(final)
print("The encoding url is : ",encodingurl)
decodingurl = urllib.parse.unquote_plus(encodingurl)
print("The decoding url is ",decodingurl)