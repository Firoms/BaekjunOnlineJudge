# 수 정렬하기 3
import sys
T = int(sys.stdin.readline())
num_dic = {}
for i in range(T):
    num = int(sys.stdin.readline())
    num_dic[num] = num_dic.setdefault(num,0) + 1
for key, val in sorted(num_dic.items()):
    for i in range(val):
        print(key)
