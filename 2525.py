# 오븐 시계
import sys

H, M = map(int, sys.stdin.readline().split(" "))
P = int(sys.stdin.readline().rstrip())
new_H = (H + (M + P) // 60) % 24
new_M = (M + P) % 60
print(new_H, new_M)
