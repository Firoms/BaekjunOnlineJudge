# 폭죽쇼
import sys

N, C = map(int, sys.stdin.readline().split())
time = [0] * (C + 1)
for _ in range(N):
    i = int(sys.stdin.readline().rstrip())
    for j in range(i, C + 1, i):
        time[j] = 1
print(sum(time))
