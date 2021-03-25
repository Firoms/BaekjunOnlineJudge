# 동전 0
import sys
import copy
import math


N, K = map(int, sys.stdin.readline().split())
coin_li = []    
for i in range(N):
    coin = int(sys.stdin.readline().rstrip())
    if coin <= K:
        coin_li.append(coin)
coin_li.reverse()
pop_li = [[i] for i in coin_li]

def get_lcm(arr):
    def lcm(x,y):
        return x* y // math.gcd(x,y)
    
    while True:
        arr.append(lcm(arr.pop(), arr.pop()))
        if len(arr) == 1:
            return arr[0]

get_li = copy.deepcopy(coin_li)
fast = get_lcm(get_li)
add = (K//fast)*(fast//coin_li[0])
K = K%fast

suc_li = 0
while pop_li:
    li = pop_li.pop(0)
    for i in coin_li:
        if li[-1]<i:
            continue
        new_li = copy.deepcopy(li)
        new_li.append(i)
        if sum(new_li)==K:
            if suc_li==0 or len(new_li) < len(suc_li):
                suc_li = new_li
        elif sum(new_li)<=K:
            if suc_li==0 or len(new_li) < len(suc_li):
                pop_li.append(new_li)
print(len(suc_li)+add)



