# 연도 진행바
import datetime
import sys

Month, Day, Year, Time = sys.stdin.readline().split(" ")
Month_dict = {
    'January':1,
    'February':2,
    'March':3,
    'April':4,
    'May':5,
    'June':6,
    'July':7,
    'August':8,
    'September':9,
    'October':10,
    'November':11,
    'December':12,
}
Year = int(Year)
Month = Month_dict[Month]
Day = int(Day[:-1])
H, M = map(int, Time.split(":"))
start = datetime.datetime(Year, 1, 1, 0, 0)
finish = datetime.datetime(Year, Month, Day, H, M)
total = datetime.datetime(Year+1, 1, 1, 0, 0)
print((finish-start)/(total-start)*100)