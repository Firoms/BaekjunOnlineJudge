# 폭죽쇼

import sys

T, Last = map(int, sys.stdin.readline().split())
time = []

for i in range(T):
    a = int(sys.stdin.readline().rstrip())
    for j in range(a, Last + 1, a):
        if j not in time:
            time.append(j)

print(len(time))
