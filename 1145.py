# 적어도 대부분의 배수
import sys

numList = list(map(int, sys.stdin.readline().split()))
num = min(numList)
while True:
    div = 0
    for i in range(5):
        if num % numList[i] == 0:
            div += 1
    if div > 2:
        print(num)
        break
    num += 1