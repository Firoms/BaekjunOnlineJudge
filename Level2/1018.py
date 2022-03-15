# 체스판 다시 칠하기
import sys

N, M = map(int, sys.stdin.readline().split())
min_change = 64


for n in range(N-7):
    for m in range(M-7):

        checking = True # True는 B, False는 W 
        for i in range(8):
            checking = not checking
            for j in range(8):
                pass