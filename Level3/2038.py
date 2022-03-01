# 골롱 수열

import sys

n = int(sys.stdin.readline().rstrip())


nums = [1]
result = 1
i = 0
while nums[-1] < n:
    i += 1
    if i in nums:
        result += 1
    nums.append(nums[-1] + result)
print(len(nums))
