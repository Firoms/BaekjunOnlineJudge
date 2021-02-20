# 쿠폰
import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    P = float(sys.stdin.readline().rstrip())
    print("$",end='')
    print('%.2f' %(round(P*80/100,2)))