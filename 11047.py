# 동전 0
import sys
N, K = map(int, sys.stdin.readline().split())
coin_li = []

for i in range(N):    
    coin = int(sys.stdin.readline())
    if coin < K : coin_li.append(coin)
coin_li.reverse()
for i in coin_li:
    if K%i==0:
        a = i
        break

dic = {a:1}



for i in range(a*2, K+1, a):
    min_li = []
    if i in coin_li:
        dic[i]=1
        continue
    for j in coin_li:
        if i-j in dic.keys():
            min_li.append(dic[i-j])
    dic[i]=min(min_li)+1
print(dic[K])
