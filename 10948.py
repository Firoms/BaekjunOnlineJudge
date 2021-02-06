# Daily 로또
import random
ran_nums = (random.sample(range(1, 46), 6))
ran_nums.sort()
last = ran_nums.pop()
for i in ran_nums:
    print(i, end=" ")
print(last)