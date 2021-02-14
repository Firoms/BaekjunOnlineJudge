# 세금
import sys
a = int(sys.stdin.readline().rstrip())
print(a*78//100,a*80//100 + a*20//100*78//100)