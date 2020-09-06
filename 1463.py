a = int(input())
num = a
time = 0
while num != 1:
    if num % 3 == 0:
        num = num/3
    elif num % 2 == 0:
        num = num/2
    else:
        num -= 1
    time += 1
seq = time

for i in range(a-time, a):
    newtime = 0
    num = i
    while num != 1:
        if num % 3 == 0:
            num = num/3
        elif num % 2 == 0:
            num = num/2
        else:
            num -= 1
        newtime += 1
    if a-i+newtime < time:
        time = a-i+newtime
print(time)
