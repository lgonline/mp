__author__ = 'Administrator'

import time
import datetime

def timestamp_datetime(value):
    format = '%Y-%m-%d %H:%M:%S'
    value = value//1000
    value = time.localtime(value)
    dt = time.strftime(format, value)
    return dt

def datetime_timestamp(dt):
    time.strptime(dt, '%Y-%m-%d %H:%M:%S')
    s = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S'))
    return int(s)

if __name__ == '__main__':
    #d = datetime_timestamp('2012-03-28 06:53:40')
    #print d
    stamptime1 = timestamp_datetime(1439934630005)
    print(stamptime1)