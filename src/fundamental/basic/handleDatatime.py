__author__ = 'Administrator'

from datetime import datetime,timedelta,timezone

now = datetime.now()
print('the current time is : ',now)

selfTime = datetime(2015,8,30,19,20,30)
print('my self-define time is : ',selfTime)

def changeTimestamp(selfTime):
    return selfTime.timestamp()
print('The selfTime to change datastamp is : ',changeTimestamp(selfTime))

selfTimestamp = changeTimestamp(selfTime)
def returnTimedatetime(selfTimestamp):
    return datetime.fromtimestamp(selfTimestamp)
print('The selfTimestamp to change datatiem is : ',returnTimedatetime(selfTimestamp))

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print('2015-6-1 18:19:59 to datetime is : ',cday)

print('change current time from datetime to str is : ',now.strftime('%a, %b %d %H:%M'))

print('--------------change local time to UTC time--------------------')
tz_utc_8 = timezone(timedelta(hours = 8))
lttoutc = now.replace(tzinfo=tz_utc_8)
print('local time is : ',now)
print('changed UTC time is : ',lttoutc)

print('---------------change time zone--------------------------------')
utctime = datetime.utcnow().replace(tzinfo=timezone.utc)
bjtime = utctime.astimezone(timezone(timedelta(hours=8)))
print('the current utc time is : ',utctime)
print('change utc time to bj time is : ',utctime.astimezone(timezone(timedelta(hours = 8))))