# 3대 측정
import sys

N, K, L = map(int, sys.stdin.readline().split())
pass_li = []
for _ in range(N):
    P = list(map(int, sys.stdin.readline().split()))
    if P[0] < L:
        continue
    if P[1] < L:
        continue
    if P[2] < L:
        continue
    if sum(P) < K:
        continue
    pass_li += P
print(len(pass_li) // 3)
for i in pass_li:
    print(i, end=" ")
