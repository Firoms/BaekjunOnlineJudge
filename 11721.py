a = input()
time = (len(a) + 1) // 10
for i in range(len(a)):
    print(a[i], end="")
    if (i + 1) % 10 == 0:
        print()
