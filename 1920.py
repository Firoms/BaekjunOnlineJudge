import sys
N = sys.stdin.readline().rstrip()
A = sys.stdin.readline().rstrip().split(" ")
M = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip().split(" ")
for i in B:
    if A.count(i)==0:
        print(0)
    else:
        print(1)