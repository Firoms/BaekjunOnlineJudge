# 시험 점수
import sys

mingukList = list(map(int, sys.stdin.readline().split(" ")))
manseList = list(map(int, sys.stdin.readline().split(" ")))
print(max([sum(mingukList), sum(manseList)]))
