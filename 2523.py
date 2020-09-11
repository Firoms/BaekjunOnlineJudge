a = int(input())
if a != 1:
    for i in range(a):
        print("*"*(i+1), end=" \n")

    for i in range(1, a-1):
        print("*"*(a-i), end="\n")
print("*", end="")
