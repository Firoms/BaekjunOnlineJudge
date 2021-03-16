# 모음의 개수
import sys
from collections import defaultdict
check = ['A', 'E', 'O', 'U', 'I', 'a', 'e', 'o', 'u', 'i']
T = sys.stdin.readline().rstrip()
while T!='#':
    alp_dict = defaultdict(int)
    for i in T:
        if i in check:
            alp_dict[i] += 1
    dict_sum = [i for i in alp_dict.values()]
    print(sum(dict_sum))
    T = sys.stdin.readline().rstrip()
