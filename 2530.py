# 인공지능 시계
import sys
H, M, S = map(int, sys.stdin.readline().split(" "))
P = int(sys.stdin.readline().rstrip())
new_S = (S+P)%60
new_M = ((S+P)//60+M)%60
new_H = (((S+P)//60+M)//60+H)%24
print(new_H,new_M,new_S)