T = int(input())
for i in range(T):
    a, b = input().split(" ")
    a = int(a)

    for q in b:
        print(q * a, end="")
    print()
