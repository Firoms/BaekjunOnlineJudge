a = int(input())
time = 0
li = [2**i for i in range(20)]
li += [3**i for i in range(13)]
li.sort(reverse=True)
print(li)
while a != 1:
    if a % 9 == 0:
        a = a/3
    elif a % 4 == 0:
        a = a / 2
    elif a % 3 == 0:
        a = a/3
    elif (a-1) % 9 == 0:
        a -= 1
    elif a % 2 == 0:
        a = a/2
    else:
        a -= 1

    time += 1

print(time)
