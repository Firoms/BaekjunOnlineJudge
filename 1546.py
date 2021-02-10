c = int(input())
li = input().split(" ")
for i in range(len(li)):
    li[i] = int(li[i])
li.sort()
for i in range(len(li)):
    li[i] = int(li[i]) / int(li[-1]) * 100
a = 0
for i in li:
    a += float(i)
print(a / c)
