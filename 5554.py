# 심부름 가는길
import sys

sec_li = []
for _ in range(4):
    sec_li.append(int(sys.stdin.readline()))
print(sum(sec_li) // 60)
print(sum(sec_li) % 60)
