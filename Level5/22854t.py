# 고장난 계산기 테스트

import sys
sys.setrecursionlimit(10**7)
N, Q = map(int, sys.stdin.readline().split())
original_formula = sys.stdin.readline().rstrip()


def calculator(formula, l, r, x):
    final = '+'
    new_formula = ''
    zero_check = False
    for i in range(len(formula)):
        if formula[i]=='+'or formula[i]=='*':
            if final[-1]=='+' or final[-1]=='*':
                pass
            else:
                final+=formula[i]
        else:
            if final[-1]=='+' or final[-1]=='*':
                if formula[i]!='0':
                    final+=formula[i]
                else:
                    zero_check = True
            else:
                final+= formula[i]
        if l-1<=i and i<=r-1:
            if formula[i]=='+':
                idx_num = 10
            elif formula[i]=='*':
                idx_num = 11
            else:
                idx_num = int(formula[i])
            new_num = (idx_num + x)%12
            if new_num==10:
                new_formula+='+'
            elif new_num==11:
                new_formula+='*'
            else:
                new_formula+=str(new_num)
        else:
            new_formula += formula[i]

    final = final[1:]
    if final:
        if final[-1]=='+' or final[-1]=='*':
            final = final[0:-1]
        print(eval(final)%(10**9+7))
    else:
        if zero_check:
            print(0)
        else:
            print(-1)
    return new_formula


cur_formula = original_formula
for i in range(Q):
    l, r, x = map(int, sys.stdin.readline().split())
    next_formula = calculator(cur_formula, l, r, x)
    cur_formula = next_formula
last_formula = calculator(cur_formula, 0, 0, 0)