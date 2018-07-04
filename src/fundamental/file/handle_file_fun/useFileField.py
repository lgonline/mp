__author__ = 'Administrator'
import os
from os import path

print('The os type is : ',os.name)
#print('The environment path is : ',os.environ)
print('Get the value of environment path, such as Java_home is :',os.environ.get("JAVA_HOME"))
print('Review the abspath in current field is : ',path.abspath('.'))
#print('show all of the filed in current field is : ',path.join('.','aaa'))
#print('add a new field in current field is : ',os.mkdir('D:\\IdeaProjects\\mp\\src\\file\\aaa'))
print('remove a new field in current field is : ')
print('split a field and file is : ',path.split('D:\\IdeaProjects\\mp\\src\\file\\useFileField.py'))
print('split a field and file is : ',path.splitext('D:\\IdeaProjects\\mp\\src\\file\\useFileField.py'))

print([x for x in os.listdir('D:\\IdeaProjects\\mp\\src\\') if os.path.isdir(x)])
#print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])