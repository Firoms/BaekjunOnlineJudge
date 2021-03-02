# 감정이입
import sys

A = "0b" + str(sys.stdin.readline().rstrip())
B = "0b" + str(sys.stdin.readline().rstrip())
A = int(A, 2)
B = int(B, 2)
print(format(A * B, "b"))
