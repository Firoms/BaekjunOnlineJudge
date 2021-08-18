# 교환 (실패)
# 반례 2133 2 >> 3321
import sys
def exchange():
    N, K = map(int, sys.stdin.readline().split())
    nums = []
    saveNums = []
    for i in str(N):
        nums.append(int(i))
    if len(nums)<=1:
        return -1
    for _ in range(K):
        reverseNum = list(reversed(nums))
        while nums[0]==max(nums) and len(nums)>2:
            saveNums.append(nums.pop(0))
        if len(nums)==2:
            if nums[1]==0 and saveNums==[]:
                return -1
            nums[0], nums[1] = nums[1], nums[0]
            continue
        idx = len(nums)-reverseNum.index(max(nums))-1
        nums[0], nums[idx] = nums[idx], nums[0]
        saveNums.append(nums.pop(0))
    exchangedNum = "".join([str(_) for _ in saveNums+nums])
    return exchangedNum


print(exchange())