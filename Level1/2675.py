# 문자열 반복
T = int(input())
for i in range(T):
    R, S = input().split(" ")
    R = int(R)

    for j in S:
        print(j * R, end="")
    print()
