# 골롱 수열
import sys

n = int(sys.stdin.readline().rstrip())


def golomb_recursion(pre, cur):
    if cur[0] <= n <= cur[1]:
        return 0
    
    sum_pre = sum([i for i in range(pre[0], pre[1]+1)])



golomb_recursion([2, 2], [3, 3])