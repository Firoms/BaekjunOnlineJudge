# 36진수
import sys
from collections import defaultdict

N = int(sys.stdin.readline().rstrip())

nums = []
nums_36_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 
                'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 
                'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 
                'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35
                }


for _ in range(N):
    nums.append(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())
nums = sorted(nums, key=len, reverse=True)
print(nums)



sum_nums = 0
len_num = 50
while len_num > 0:
    first_nums = defaultdict(int)

    for idx in range(len(nums)):
        if len(nums[idx])==len_num:
            first_nums[nums[idx][0]] += 1
            if len_num!=1:
                nums[idx] = nums[idx][1:]
            else:
                nums[idx] = ''
        else:
            break


    len_num -= 1