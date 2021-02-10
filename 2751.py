import sys

T = int(sys.stdin.readline())
li = []
for i in range(T):
    li.append(int(sys.stdin.readline()))
li.sort()
for i in li:
    print(i)
