# 소인수분해
A = int(input())
while A != 1:
    b = 1
    while True:
        b += 1
        if A % b == 0:
            print(b)
            A = A // b
            break
