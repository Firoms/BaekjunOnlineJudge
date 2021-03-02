# FA
import sys

num = int(sys.stdin.readline().rstrip())
num_li = [num]


def F(x):
    F_num = int(str(x)[0]) * len(str(x))
    if F_num == num_li[-1]:
        return print("FA")
    elif F_num in num_li:
        return print("NFA")
    else:
        num_li.append(F_num)
        F(F_num)


F(num)
