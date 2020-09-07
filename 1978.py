T = int(input())
li = list(map(int, input().split(" ")))
for i in range(2, 501):
    a = [j*i for j in range(2, 501)]
    li = list(set(li) - set(a))
li.sort()
try:
    li.remove(1)
except:
    pass
print(len(li))
