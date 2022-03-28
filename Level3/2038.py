# 골롱 수열
import sys

n = int(sys.stdin.readline().rstrip())
suyeol = [0]*(n+1)


suyeol[1], suyeol[2], suyeol[3] = 1, 2, 2
idx = 3
last = 4
while suyeol[n]==0:
    suyeol[last : last + suyeol[idx]] = [idx for _ in range(suyeol[idx])]
    last += suyeol[idx]
    idx += 1

print(suyeol[n])