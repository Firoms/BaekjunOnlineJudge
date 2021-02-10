import copy

li = []
for i in range(9):
    li.append(int(input()))
re = copy.deepcopy(li)
li.sort()
print(li[-1])
print(re.index(li[-1]) + 1)
