# 24
from datetime import time
import sys

sH, sM, sS = map(int, sys.stdin.readline().split(":"))
nH, nM, nS = map(int, sys.stdin.readline().split(":"))



start_time = time(sH, sM, sS)
now_time = time(nH, nM, nS)

time_difference = now_time - start_time
print(time_difference)
