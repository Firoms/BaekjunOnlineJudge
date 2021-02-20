# 체스판 조각
import sys

T = int(sys.stdin.readline().rstrip())
print((T // 2 + 1) * (T // 2 + T % 2 + 1))
