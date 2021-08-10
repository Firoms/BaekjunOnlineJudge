# 명령 프롬프트
import sys

T = int(sys.stdin.readline().rstrip())
fWord = [i for i in sys.stdin.readline().rstrip()]
for _ in range(T - 1):
    nWord = sys.stdin.readline().rstrip()
    for i in range(len(nWord)):
        if fWord[i] != nWord[i]:
            fWord[i] = "?"
for i in fWord:
    print(i, end="")
