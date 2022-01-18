# 타임머신
from datetime import time
import sys

times = list(map(int, sys.stdin.readline().split(":")))
times.sort()
if times[-1]>59 or times[0]<1 or time[0]>12:
    print("0")

