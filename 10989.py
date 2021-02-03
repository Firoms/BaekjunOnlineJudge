# 수 정렬하기 3
import sys
T = int(sys.stdin.readline())
li = []
for i in range(T):
    li+=[int(sys.stdin.readline())]
for i in range(10001):
    while True:
        try:
            li.remove(i)
            print(i)
        except:
            break