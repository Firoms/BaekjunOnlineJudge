T = int(input())
time = 0
for i in range(T):
    a = input()
    li = []
    for i in range(len(a)):
        try:
            if i == 0:
                li.append(a[i])
                continue
            if a[i] == a[i - 1]:
                pass
            else:
                if a[i] in li:
                    time -= 1
                    break
                li.append(a[i])
        except:
            pass

    time += 1
print(time)
