# 다리 놓기
import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    M, N = map(int, sys.stdin.readline().split())
    cnt = 1
    for n in range(M):
        cnt *= N - n
        cnt /= n + 1
    print(int(cnt))
