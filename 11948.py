# 과목선택
import sys
s1 = []
s2 = []
for i in range(4):
    s1.append(int(sys.stdin.readline().rstrip()))
for i in range(2):
    s2.append(int(sys.stdin.readline().rstrip()))
s1.remove(min(s1))
s2.remove(min(s2))
print(sum(s1)+sum(s2))