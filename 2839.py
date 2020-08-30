a = int(input())
fi = a//5
five = 0
three = 0
for i in range(fi):
    if (a-(fi-i)*5) % 3 == 0:
        five = fi-i
        three = (a-(fi-i)*5)//3
        print(five+three)
        break
if five == 0:
    if a % 3 == 0:
        print(a//3)
    else:
        print("-1")
