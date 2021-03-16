# 부호
import sys
for _ in range(3):
    T = int(sys.stdin.readline().rstrip())
    num_li = []
    for i in range(T):
        num_li.append(int(sys.stdin.readline().rstrip()))
    result = sum(num_li)
    if result>0:
        print("+")
    elif result==0:
        print(0)
    else:
        print("-")