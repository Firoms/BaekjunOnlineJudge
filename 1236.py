# 성 지키기
import sys

N, M = map(int, sys.stdin.readline().split())
N_list = [i for i in range(N)]
M_list = [i for i in range(M)]
for i in range(N):
    R = sys.stdin.readline().rstrip()
    for j in range(M):
        if R[j] == "X":
            if i in N_list:
                N_list.remove(i)
            if j in M_list:
                M_list.remove(j)
print(max([len(N_list), len(M_list)]))
