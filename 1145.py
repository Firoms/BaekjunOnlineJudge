# 적어도 대부분의 배수
import sys
num_li = list(map(int, sys.stdin.readline().split()))
num = min(num_li)
while True:
    div = 0
    for i in range(5):
        if num%num_li[i]==0:
            div+=1
    if div>2:
        print(num)
        break
    num+=1