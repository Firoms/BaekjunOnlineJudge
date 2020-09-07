T = int(input())


# def fac(num):
#     if num == 1:
#         return 1
#     return num*fac(num-1)


# print(fac(T))
a = 1
for i in range(2, T+1):
    a *= i
print(a)
