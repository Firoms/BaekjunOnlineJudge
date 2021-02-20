# 17배
import sys

num2 = "0b" + str(sys.stdin.readline().rstrip())

print(format(int(num2, 2) * 17, "b"))
