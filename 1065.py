a = int(input())
han = 0
for i in range(1, a+1):
    if i > 99:
        str_i = str(i)
        d = int(str_i[1])-int(str_i[0])
        for k in range(2, len(str_i)):
            if int(str_i[k]) != int(str_i[k-1])+d:
                han -= 1
                break
    han += 1
print(han)
