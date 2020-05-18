b = input().split(' ')
N, X = list(map(int, b))
A = input().split(' ')
A = list(map(int, A))

for i in A :
    if i< X :
        print(i, end=(" "))