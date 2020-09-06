li = []
re_li = []
for i in range(10):
    li.append(int(input()))
for i in li:
    re_li.append(i % 42)
re_li = set(re_li)
print(len(re_li))
