# 농구 경기
import sys
from collections import defaultdict
N = int(sys.stdin.readline().rstrip())
pla_dic = defaultdict(int)
for _ in range(N):
    pla_dic[sys.stdin.readline()[0]]+=1
f_li = []
for key, value in pla_dic.items():
    if value>=5:
        f_li.append(key)
f_li.sort()
for i in f_li:
    print(i, end="")
if len(f_li)==0:
    print("PREDAJA")