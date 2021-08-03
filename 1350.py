# 진짜 공간
import sys
N = int(sys.stdin.readline().rstrip())
files = list(map(int, sys.stdin.readline().rstrip().split()))
file_size = int(sys.stdin.readline().rstrip())
save_size = 0
for file in files:
    if file != 0:
        if file%file_size!=0:
            save_size += file_size*(file//file_size+1)
        else:
            save_size += file_size*(file//file_size)
print(save_size)