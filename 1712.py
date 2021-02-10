import sys

A, B, C = map(int, (sys.stdin.readline().rstrip()).split(" "))
if B >= C:
    print("-1")
else:
    a = A // (C - B) + 1
    print(a)
