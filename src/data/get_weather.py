#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

from urllib.request import urlopen
from bs4 import BeautifulSoup

webpage = urlopen("https://www.wunderground.com/history/airport/KBUF/2016/4/1/DailyHistory.html")
soup = BeautifulSoup(webpage)
#nobrs = soup.find_all(attrs={'class':'nobr'})

if __name__ == "__main__":
    print(soup)
    #print(nobrs[4])