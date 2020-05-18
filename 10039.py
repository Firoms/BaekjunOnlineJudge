score_list = []
for i in range(5) :
    score_list.append(int(input()))


def avg(scores) :
    total = 0
    for single_score in scores :
        if single_score < 40 :
            total += 40
        else :
            total += single_score
    average = int(total/5)
    return average


print(avg(score_list))


# a =int(input())
# b =int(input())
# c =int(input())
# d =int(input())
# e =int(input())

# total = 0
#
# def f(k):
#     global total
#     if k>40 :
#         total += k
#     else :
#         total += 40

# f(a)
# f(b)
# f(c)
# f(d)
# f(e)
# total = int(total/5)
# print(total)

