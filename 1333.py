# 부재중 전화
import sys


def notice_call():
    N, L, D = map(int, sys.stdin.readline().split(" "))
    break_start = -5
    for _ in range(N):
        break_start += (L+5)
        break_finish = break_start + 5
        for i in range(break_start, break_finish):
            if i%D==0:
                print(i)
                return
    while True:
        if break_finish%D==0:
            print(break_finish)
            return
        break_finish += 1
notice_call()