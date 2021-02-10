# 통계학
import sys

N = int(sys.stdin.readline().rstrip())
num_li = []
num_dic = {}
for i in range(N):
    num = int(sys.stdin.readline().rstrip())
    num_li.append(num)
    num_dic[num] = num_dic.setdefault(num, 0) + 1
num_li.sort()
sort_dic = sorted(num_dic.items(), key=lambda x: x[1], reverse=True)
many = sort_dic[0][1]
many_li = []
for i in range(len(sort_dic)):
    if sort_dic[i][1] == many:
        many_li.append(sort_dic[i][0])
    else:
        break
many_li.sort()

print(round(sum(num_li) / N))
print(num_li[N // 2])
try:
    print(many_li[1])
except:
    print(many_li[0])
print(max(num_li) - min(num_li))
