# 1로 만들기
import sys

num = int(sys.stdin.readline())
cnt_list = [0, 0]

for i in range(2, num + 1):
    if i % 3 == 0 and i % 2 == 0:
        cnt_list.append(min(cnt_list[i // 3], cnt_list[i // 2], cnt_list[i - 1]) + 1)

    elif i % 3 == 0:
        cnt_list.append(min(cnt_list[i // 3], cnt_list[i - 1]) + 1)
    elif i % 2 == 0:
        cnt_list.append(min(cnt_list[i // 2], cnt_list[i - 1]) + 1)
    else:
        cnt_list.append(cnt_list[i - 1] + 1)

print(cnt_list[-1])
