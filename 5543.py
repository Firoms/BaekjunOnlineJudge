li1 = []
li2 = []
for i in range(3):
    li1.append(int(input()))
for i in range(2):
    li2.append(int(input()))
li1.sort()
li2.sort()
print(li1[0] + li2[0] - 50)
