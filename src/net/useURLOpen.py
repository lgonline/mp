__author__ = 'Administrator'

from urllib import request
import urllib
#response = request.urlopen("https://www.baidu.com/")
#html = response.read()
#print(html)

urllib.urlretrieve("https://www.baidu.com","d:\\baidu.html")