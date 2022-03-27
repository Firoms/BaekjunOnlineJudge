# 골롱 수열
import sys

n = int(sys.stdin.readline().rstrip())


def golomb_recursion(pre, cur):
    if cur[0] <= n <= cur[1]:
        return 0

    sum_pre = sum([i for i in range(pre[0], pre[1] + 1)])
    len_cur = cur[1] - cur[0] + 1
    len_pre = pre[1] - pre[0] + 1

    len_new_cur = sum_pre * len_cur / len_pre

    golomb_recursion(cur, new_cur)


golomb_recursion([2, 2], [3, 3])
