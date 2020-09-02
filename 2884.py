a, b = map(int, input().split(" "))
c = a * 60 + b
c -= 45
a = c//60
b = c % 60
if c < 0:
    a = 23
    b = 60+c
print(a, b)
