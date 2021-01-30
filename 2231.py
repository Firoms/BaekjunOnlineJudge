N = int(input())
check_start = N-(len(str(N))*9)
if check_start <= 0:
    check_start = 1

bunbaehap = 0
for i in range(check_start, N):
    bunbaehap = 0
    for j in str(i):
        bunbaehap += int(j)
    bunbaehap += i
    if bunbaehap == N:
        print(i)
        break
if bunbaehap!=N:
    print(0)