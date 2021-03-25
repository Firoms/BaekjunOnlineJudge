# 임시 반장 정하기
import sys
from collections import defaultdict
S = int(sys.stdin.readline().rstrip())
stu_classes = []
friend_dict = defaultdict(list)

for _ in range(S):
    classes = list(map(int, sys.stdin.readline().split()))
    for stu_idx in range(len(stu_classes)):
        for i in range(5):
            if stu_classes[stu_idx][i]==classes[i]:
                friend_dict[stu_idx+1].append(len(stu_classes)+1)
                friend_dict[len(stu_classes)+1].append(stu_idx+1)
                break
    stu_classes.append(classes)
max_value = 0
max_key = [1]
for key, value in friend_dict.items():
    if len(value)>max_value:
        max_value = len(value)
        max_key=[key]
    elif len(value)==max_value:
        max_key.append(key)
print(min(max_key))