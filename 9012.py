T = int(input())
for k in range(T):
    r = True
    a = input()
    li = []
    for i in a:
        if i == '(':
            li.append(')')
        elif i == ')':
            try:
                li.pop(-1)
            except:
                r = False
                break
    if r == True and len(li) == 0:
        print("YES")
    else:
        print("NO")
