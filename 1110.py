a = int(input())
answer = a
cnt = 0
while True :

    b = int(a/10)
    c = int(a%10)
    d = b+c
    e = d%10
    a = 10*c + e
    cnt += 1
    if a == answer :
        break
print(cnt)

