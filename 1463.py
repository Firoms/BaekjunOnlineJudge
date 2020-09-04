a = int(input())
li = []
# j = a-10
# if j <= 0:
#     j = 1
for i in range(a-9, a+1):
    time = 0
    num = i
    while num != 1:
        if num % 3 == 0:
            num = num/3
        elif num % 2 == 0:
            num = num/2
        else:
            num -= 1
        time += 1
    li.append(time)
    for k in range(0, len(li)-1):
        if li[-1] > li[k] + 9-k:
            li[-1] = li[k] + 9-k
        # if li[-1] > li[k] + i - (k+1):
        #     li[-1] = li[k] + i - (k+1)
print(li[-1])
