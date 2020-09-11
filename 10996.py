a = int(input())
for i in range(a):
    if a % 2 == 1:
        print("* "*(a//2+1))
        print(" ", end="")
        print("* "*(a//2-1), end="")
    else:
        print("* "*(a//2))
        print(" ", end="")
        print("* "*(a//2-1), end="")
    if a > 1:
        print("*")
