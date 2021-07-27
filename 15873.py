# 공백 없는 A+B
import sys

C = sys.stdin.readline().rstrip()

if len(C) == 3:
    if int(C[1:3]) == 10:
        print(int(C[0]) + int(C[1:3]))
    else:
        print(int(C[0:2]) + int(C[2]))
elif len(C) == 4:
    print(20)
else:
    print(int(C[0]) + int(C[1]))
