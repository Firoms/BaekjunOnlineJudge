# 파일 옮기기
import sys

A1, B1 = map(int, sys.stdin.readline().split())
A2, B2 = map(int, sys.stdin.readline().split())
print(min([A1 + B2, A2 + B1]))
