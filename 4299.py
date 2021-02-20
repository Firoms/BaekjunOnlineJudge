# AFC 윔블던
import sys

P, M = map(int, sys.stdin.readline().split(" "))
if (P + M) % 2 != 0 or (P - M) % 2 != 0 or P < M:
    print(-1)
else:
    print((P + M) // 2, (P - M) // 2)
