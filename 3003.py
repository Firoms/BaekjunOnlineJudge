# 킹, 퀸, 룩, 비숍, 나이트, 폰
import sys

K, Q, L, B, N, P = map(int, sys.stdin.readline().split(" "))
print(1 - K, 1 - Q, 2 - L, 2 - B, 2 - N, 8 - P)
