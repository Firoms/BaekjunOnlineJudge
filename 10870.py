# 피보나치 수 5
def fibo(num):
    if num == 0 or num == 1:
        return num
    return fibo(num - 1) + fibo(num - 2)


print(fibo(int(input())))
