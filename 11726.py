a = int(input())
b = a//2
times = 0
while b > -1:
    c = a-(2*b)
    time = 1
    for i in range(1, c+b+1):
        time *= i
    for j in range(1, c+1):
        time //= j
    for k in range(1, b+1):
        time //= k
    times += time
    b -= 1
print(int(times) % 10007)
