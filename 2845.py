# 파티가 끝나고 난 뒤
import sys

A, I = map(int, sys.stdin.readline().split(" "))
li = list(map(int, sys.stdin.readline().split(" ")))
for i in li:
    print(i - (A * I), end=" ")
