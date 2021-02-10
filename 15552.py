import sys

T = int(input())
for i in range(T):
    a, b = (sys.stdin.readline().rstrip()).split(" ")
    print(int(a) + int(b))
