# 제곱 ㄴㄴ 수 (실패)
# 반례, 세제곱, 네제곱등도 고려


import sys

minNum, maxNum = map(int, sys.stdin.readline().split())
noNum = 0
for i in range(minNum, maxNum + 1):
    if i ** 0.5 != int(i ** 0.5):
        noNum += 1
print(noNum)
