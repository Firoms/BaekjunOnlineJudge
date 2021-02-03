# 통계학
from collections import Counter
N = int(input())
num_li = []
for i in range(N):
    num_li.append(int(input()))
num_li.sort()
print(sum(num_li)//len(num_li))
print(num_li[len(num_li)//2])
cnt = Counter(num_li)
most = cnt.most_common()
most_list = []
for j in most:
    if j[1]== most[0][1]:
        most_list.append(j[0])
most_list.sort()
if len(most_list) > 1:
    print(most_list[1])
else:
    print(most_list[0])
print(max(num_li)-min(num_li))