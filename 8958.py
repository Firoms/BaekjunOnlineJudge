T = int(input())
for i in range(T):
    a = input()
    b = []
    b = a.split("X")
    osum = 0
    for j in b:
        for k in range(len(j)):
            osum += k + 1
    print(osum)
