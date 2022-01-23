# 타임머신
import sys

times = list(map(int, sys.stdin.readline().split(":")))
times.sort()
if times[2] > 59 or times[0] < 0 or times[0] > 12 or times[2]==0:
    print(0)
elif times[0]==times[1] and times[1]==times[2]:
    print(1)
elif times[0]==times[1] or times[1]==times[2] or times[0]==times[2]:
    if times[1]==0:
        print(2)
    elif times[1]<=12:
        print(4)
    else:
        print(2)
else:
    if times[2]<=12:
        print(6)
    elif times[1]<=12:
        print(4)
    else:
        print(2)