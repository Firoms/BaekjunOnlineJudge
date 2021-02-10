# 탑
import sys

N = sys.stdin.readline()

tower_li = list(map(int, sys.stdin.readline().split()))
tower_dic = {}
tower_check = list(tower_li)
stack = []
while tower_check:
    tower_num = len(tower_check)
    tower = tower_check.pop()
    while stack:
        if stack[-1] < tower:
            tower_dic[stack[-1]] = tower_num
            stack.pop()
        else:
            break
    stack.append(tower)
for i in stack:
    tower_dic[i] = 0
for i in tower_li:
    print(tower_dic[i], end=" ")
