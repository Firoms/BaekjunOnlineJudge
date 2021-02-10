# 바이러스
import sys


def find_virus(info, virus):
    virus_list = []
    first = info[virus]

    def find(names):
        for i in names:
            second = info[i]
            if i not in virus_list:
                virus_list.append(i)
                find(second)

    find(first)
    print(len(virus_list) - 1)


N = int(sys.stdin.readline())
C = int(sys.stdin.readline())

com_info = {}
for _ in range(C):
    com1, com2 = map(int, sys.stdin.readline().split())
    if com1 in com_info:
        com_info[com1].append(com2)
    else:
        com_info[com1] = [com2]
    if com2 in com_info:
        com_info[com2].append(com1)
    else:
        com_info[com2] = [com1]


find_virus(com_info, 1)
