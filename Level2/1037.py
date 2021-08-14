# 약수
import sys

amount = sys.stdin.readline().rstrip()
divisors = list(map(int, sys.stdin.readline().split()))

if len(divisors) == 1:
    print(divisors[0] ** 2)
else:
    print(max(divisors) * min(divisors))
