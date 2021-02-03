# 나이순 정렬
N = int(input())
user_dict = {}
for i in range(1, 201):
    user_dict[i]=[]
for i in range(N):
    a, b = input().split()
    user_dict[int(a)].append(b)
for i in range(1,201):
    for j in user_dict[i]:
        print(i, j)