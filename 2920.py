a = list(map(int, input().split(" ")))
b = len(a)
for i in range(len(a) - 1):
    if a[i] > a[i + 1]:
        b += 1
    else:
        b -= 1
if b == 1:
    print("ascending")
elif b == len(a) * 2 - 1:
    print("descending")
else:
    print("mixed")
