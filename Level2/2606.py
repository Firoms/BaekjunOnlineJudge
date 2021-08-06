# 바이러스
import sys


def findVirus(info, virus):
    virusList = []
    first = info[virus]

    def find(names):
        for i in names:
            second = info[i]
            if i not in virusList:
                virusList.append(i)
                find(second)

    find(first)
    print(len(virusList) - 1)


N = int(sys.stdin.readline())
C = int(sys.stdin.readline())

comInfo = {}
for _ in range(C):
    com1, com2 = map(int, sys.stdin.readline().split())
    if com1 in comInfo:
        comInfo[com1].append(com2)
    else:
        comInfo[com1] = [com2]
    if com2 in comInfo:
        comInfo[com2].append(com1)
    else:
        comInfo[com2] = [com1]


findVirus(comInfo, 1)
