__author__ = 'Administrator'

import os

def FileInputStream(filename):
    try:
        file = open(filename)
        for line in file:
            yield bytearray
    except StopIteration:
        file.close()
        return

def FileOutputStream(inputStream, filename):
    try:
        file = open(filename,"w")
        while True:
            byte = inputStream.next()
            file.write(byte)
    except StopIteration:
        file.close()
        return

if __name__ == "__main__":
    FileOutputStream(FileInputStream("d:\\aaa.txt"),"d:\\hello.txt")