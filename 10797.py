# 10부제
import sys
num = int(sys.stdin.readline().rstrip())
num_li = list(map(int, sys.stdin.readline().split()))
print(num_li.count(num))