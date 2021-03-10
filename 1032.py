# 명령 프롬프트
import sys
T = int(sys.stdin.readline().rstrip())
f_word = [i for i in sys.stdin.readline().rstrip()]
for _ in range(T-1):
    n_word = sys.stdin.readline().rstrip()
    for i in range(len(n_word)):
        if f_word[i] != n_word[i]:
            f_word[i]='?'
for i in f_word:
    print(i, end="")

