# 검증수
import sys
nums = list(map(int,sys.stdin.readline().split(" ")))
li = []
for i in nums:
    li.append(i**2)
print(sum(li)%10)