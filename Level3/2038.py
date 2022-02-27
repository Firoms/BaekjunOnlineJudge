# 골롱 수열

import sys
n = int(sys.stdin.readline().rstrip())

golomb = [0, 1, 2, 2]
num = 3

while len(golomb)<n:
    for _ in range(golomb[num]):
        golomb.append(num)
        
    num += 1

print(golomb)