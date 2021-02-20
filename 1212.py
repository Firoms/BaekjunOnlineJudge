# 8진수 2진수
import sys

num8 = str(sys.stdin.readline().rstrip())
print(format(int(num8, 8), "b"))
