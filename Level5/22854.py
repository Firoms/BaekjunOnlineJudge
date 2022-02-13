# 고장난 계산기 (Calculator) 게임
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
        
print(formula_list)

def calculate():
    # 1번 기본 식 정리
    real_formula = [['+']]
    for i in original_list:
        if real_formula[-1]=='+' or real_formula[-1]=='*':
            if i=='+'or i=='*':
                continue
        real_formula.append(i)
    real_formula.pop(0)