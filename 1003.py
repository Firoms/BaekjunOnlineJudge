import sys
T = int(sys.stdin.readline())


def fibonacci(n):
    if n == 0:
        dic[0] += 1
    elif n == 1:
        dic[1] += 1
    else:
        fibonacci(n-1)
        fibonacci(n-2)


for i in range(T):
    dic = {1: 0, 0: 0}
    fibonacci(int(sys.stdin.readline()))
    print(dic[0], dic[1])
