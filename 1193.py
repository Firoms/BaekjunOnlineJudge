a = int(input())
a += 1
time = 0
b = 1
i = 0
while a > b:
    b += i
    i += 1
    time += 1

b -= i - 1
c = a - b
if time % 2 == 1:
    print(f"{c}/{time-c}")
else:
    print(f"{time-c}/{c}")
