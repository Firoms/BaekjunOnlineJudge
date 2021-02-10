a = int(input())
time = 0
li = [i * 6 for i in range(1, 1600000)]
b = 1
i = 0
while a > b:
    b += li[i]
    i += 1
    time += 1
print(time + 1)
