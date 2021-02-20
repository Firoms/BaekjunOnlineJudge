# Rats
import sys

a, b, c = map(int, sys.stdin.readline().split(" "))
print(int((a + 1) * (b + 1) / (c + 1) - 1))
