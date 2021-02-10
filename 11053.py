# 가장 긴 증가하는 부분 수열
N = int(input())
su_li = list(map(int, input().split()))
num_li = []
num_li.append(1)
for i in range(1, len(su_li)):
    max_list = [1]
    for j in range(i):
        if su_li[j] < su_li[i]:
            max_list.append(num_li[j])
    if max_list != [1]:
        num_li.append(max(max_list) + 1)
    else:
        num_li.append(1)
print(max(num_li))
