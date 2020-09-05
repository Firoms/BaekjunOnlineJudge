li = [i for i in range(1, 10001)]


def d(n):
    num = n
    str_num = str(num)
    str_sum = 0
    for i in str_num:
        str_sum += int(i)
    try:
        li.remove(str_sum+num)
    except:
        pass


for i in range(10000):
    d(i)
for i in li:
    print(i)
