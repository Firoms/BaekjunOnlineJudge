# 고장난 계산기 (Calculator) 게임 (시간초과 실패)
import sys
import copy

N, Q = map(int, sys.stdin.readline().split())

original_formula = sys.stdin.readline().rstrip()
original_list = [i for i in original_formula]

formula_list = []
formula_list.append(original_list)
for _ in range(Q):
    query_list = copy.deepcopy(formula_list[-1])
    l, r, x = map(int, sys.stdin.readline().split())
    for i in range(l-1, r):
        if query_list[i]=='+':
            idx_num = 10
        elif query_list[i]=='*':
            idx_num = 11
        else:
            idx_num = int(query_list[i])
        new_num = (idx_num + x)%12
        if new_num==10:
            query_list[i]='+'
        elif new_num==11:
            query_list[i]='*'
        else:
            query_list[i]=str(new_num)
    formula_list.append(query_list)
        
# print(formula_list)

real_formula_list = []

for formula in formula_list:
    real_formula = ['+']
    for i in formula:
        if i=='+'or i=='*':
            if real_formula[-1]=='+' or real_formula[-1]=='*':
                continue
            else:
                real_formula.append(i)
        else:
            if real_formula[-1]=='+' or real_formula[-1]=='*':
                real_formula.append(i)
            else:
                if real_formula[-1]=='0':
                    real_formula[-1] = i
                else:
                    real_formula[-1] += i
    real_formula.pop(0)
    if real_formula:
        if real_formula[-1]=='+' or real_formula[-1]=='*':
            real_formula.pop(-1)

    real_formula_list.append(real_formula)

# print(real_formula_list)


for formula in real_formula_list:
    formula_str = ''
    for i in formula:
        formula_str += i
    if formula_str:
        print(eval(formula_str)%(10**9+7))
    else: 
        print(-1)