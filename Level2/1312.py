# 소수 (실패)

import sys

A, B, N = map(int, sys.stdin.readline().split())

result = str(A / B) + "0"
alp = []
for i in range(2, len(result)):
    if result[i] in alp:
        break
    else:
        alp.append(result[i])

if "0" in alp and N > len(alp):
    print(0)
else:
    print(alp[(N - 1) % (len(alp))])
