# D-Day
import datetime
import sys
Year1, Month1, Day1 = map(int, sys.stdin.readline().split(" "))
Year2, Month2, Day2 = map(int, sys.stdin.readline().split(" "))

start = datetime.date(Year1, Month1, Day1)
finsh = datetime.date(Year2, Month2, Day2)

d_day = str(finsh-start).split(" ")[0]
if int(d_day)>=365243:
    print("gg")
else:
    print(f"D-{d_day}")