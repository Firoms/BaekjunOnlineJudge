# 팀 나누기
import sys

num_li = list(map(int, sys.stdin.readline().split()))
team1 = max(num_li) + min(num_li)
num_li.remove(max(num_li))
num_li.remove(min(num_li))
print(abs(team1 - (sum(num_li))))
