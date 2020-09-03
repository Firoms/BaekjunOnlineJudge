T = int(input())
for i in range(T):
    a = input().split(" ")
    for j in range(len(a)):
        a[j] = int(a[j])
    up = 0
    avg = (sum(a)-a[0])/a[0]
    for j in range(1, len(a)):
        if a[j] > avg:
            up += 1
    result = up/a[0]*100
    print("%0.3f" % result, end="")
    print("%")
