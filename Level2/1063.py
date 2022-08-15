# 킹
import sys

K, R, T = sys.stdin.readline().split()

def move(O, lr, ud):
    alp = O[0]
    num = int(O[1])
    alp_to_num = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8}
    num_to_alp = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H'}
    
    new_alp = num_to_alp[max([min([alp_to_num[alp]+lr, 8]), 1])]
    new_num = str(max([min([num+ud, 8]), 1]))
    return new_alp + new_num


for _ in range(int(T)):
    M = sys.stdin.readline().rstrip()
    
    if M=='R':
        K = move(K, 1, 0)
    elif M=='L':
        K = move(K, -1, 0)
    elif M=='B':
        K = move(K, 0, -1)
    elif M=='T':
        K = move(K, 0, 1)
    elif M=='RT':
        K = move(K, 1, 1)
    elif M=='LT':
        K = move(K, -1, 1)
    elif M=='RB':
        K = move(K, 1, -1)
    elif M=='LB':
        K = move(K, -1, -1)
    else:
        #오류
        pass
    
print(K)