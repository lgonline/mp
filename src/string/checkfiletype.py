__author__ = 'Administrator'

print("-------welcome to file upload system-------------")
filetype = input("Please input the file path your wanted.")
if (filetype.endswith(".gif") or filetype.endswith(".jpg")):
    print("the image is current, uploading...")
else:
    print("the file is incurrent, please re-select it again.")