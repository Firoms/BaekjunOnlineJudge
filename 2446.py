a = int(input())
if a!=1:
    for i in range(a):
        print(" "*i, end="")
        print("*"*((a-i)*2-1), end="")
        print("", end=" \n")
    for i in range(1, a-1):
        print(" "*(a-i-1), end="")
        print("*"*((i+1)*2-1), end="")
        print("", end=" \n")
print("*"*((a)*2-1), end="")
