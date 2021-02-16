# 세수정렬
import sys
num_li = list(map(int, sys.stdin.readline().split(" ")))
num_li.sort()
for i in num_li:
    print(i, end= " ")