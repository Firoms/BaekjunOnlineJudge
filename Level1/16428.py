# A/B - 3
import sys
A, B = map(int, sys.stdin.readline().split())

share, left = divmod(A, B)
print(share)
print(left)