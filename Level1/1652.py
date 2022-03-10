# 누울 자리를 찾아라

import sys

N = int(sys.stdin.readline().rstrip())
wseat = 0
hseat = 0



for _ in range(N):
    line = sys.stdin.readline().rstrip()
    height = ['' for i in range(N)]
    for i in range(N):
        height[i] = height[i]+line[i]
    seat = line.split("X")
    # print(seat)
    for i in range(2, N+1):
        wseat += seat.count("."*i)
        # print(wseat, "wseat")

# print(height)
for line in height:
    seat = line.split("X")
    # print(seat)
    for i in range(2, N+1):
        hseat += seat.count("."*i)
        # print(hseat, "hseat")

# print(wseat, hseat)