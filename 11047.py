# 동전 0
N, K = map(int, input().split())
coin_li = []
for i in range(N):
    coin_li.append(int(input(i)))
coin_li.reverse()

print(coin_li)
coin = 0

for i in range(len(coin_li)):
    while coin_li[i] <= K:
        coin += 1
        K-=coin_li[i]
print(coin)