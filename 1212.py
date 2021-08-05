# 8진수 2진수

import sys
numOctal = str(sys.stdin.readline().rstrip())
print(format(int(numOctal, 8), "b"))
