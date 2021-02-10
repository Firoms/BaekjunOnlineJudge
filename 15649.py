# N과 M(1)
import sys

N, M = map(int, sys.stdin.readline().split())


def sun(num_li):
    result_li = []

    def add_sun(li, test_li):
        for i in range(len(test_li)):
            sun_li = list(li)
            add_li = list(test_li)
            if len(li) != M:
                sun_li.append(add_li.pop(i))
                add_sun(sun_li, add_li)

        if len(li) == M:
            for i in li:
                print(i, end=" ")
            print()

    for i in range(len(num_li)):
        add_li = list(num_li)
        li = [add_li.pop(i)]
        add_sun(li, add_li)


sun([i for i in range(1, N + 1)])
