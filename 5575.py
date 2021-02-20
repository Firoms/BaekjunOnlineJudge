# 타임 카드
import sys

for _ in range(3):
    time_li = list(map(int, sys.stdin.readline().split(" ")))
    h = time_li[3] - time_li[0] - 1
    m = 60 + time_li[4] - time_li[1] - 1
    s = 60 + time_li[5] - time_li[2]
    if s >= 60:
        s -= 60
        m += 1
    if m >= 60:
        m -= 60
        h += 1
    print(h, m, s)
