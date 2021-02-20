# 시험 점수
import sys

minguk_li = list(map(int, sys.stdin.readline().split(" ")))
manse_li = list(map(int, sys.stdin.readline().split(" ")))
print(max([sum(minguk_li), sum(manse_li)]))
