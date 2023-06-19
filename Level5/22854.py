# 고장난 계산기 (Calculator) 게임 <미해결>
N, Q = map(int, input().split())
formula = input()
caltree = ["" for i in range(8 * N)]
change = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "+",
    11: "*",
    12: "0",
    13: "1",
    14: "2",
    15: "3",
    16: "4",
    17: "5",
    18: "6",
    19: "7",
    20: "8",
    21: "9",
    22: "+"
}


def calmerge(left, right):
    if (left[-1] == "+" or left[-1] == "*") and (right[0] == "+" or right[0] == "*"):
        return left + right[1:]
    else:
        return left + right


def calbuild(caltree, Node, left, right):
    if left == right:
        caltree[Node] = formula[left]
        return caltree[Node]

    mid = left + (right - left) // 2
    left_val = calbuild(caltree, 2 * Node, left, mid)
    right_val = calbuild(caltree, 2 * Node + 1, mid + 1, right)
    caltree[Node] = calmerge(left_val, right_val)
    return caltree[Node]


calbuild(caltree, 1, 0, N - 1)


def calupdate(idx, val, Node, left, right):
    if idx < left or idx > right:
        return caltree[Node]

    if left == right:
        if caltree[Node] == "+":
            caltree[Node] = change[10 + val]
        elif caltree[Node] == "*":
            caltree[Node] = change[11 + val]
        else:
            caltree[Node] = change[int(caltree[Node]) + val]
        return caltree[Node]

    mid = left + (right - left) // 2
    left_val = calupdate(idx, val, 2 * Node, left, mid)
    right_val = calupdate(idx, val, 2 * Node + 1, mid + 1, right)
    caltree[Node] = calmerge(left_val, right_val)
    return caltree[Node]


def calculate(caltree_formula):
    if caltree_formula:
        if caltree_formula[0] == "*" or caltree_formula[0] == "+":
            caltree_formula = caltree_formula[1:]
    if caltree_formula:
        if caltree_formula[-1] == "*" or caltree_formula[-1] == "+":
            caltree_formula = caltree_formula[:-1]

    if caltree_formula == "":
        return -1
    else:
        while caltree_formula[0] == "0":
            if caltree_formula == "0":
                return 0
            else:
                caltree_formula = caltree_formula[1:]
        return eval(caltree_formula) % (10**9 + 7)


print(calculate(caltree[1]))

for i in range(Q):
    l, r, x = map(int, input().split())
    for j in range(l - 1, r):
        calupdate(j, x, 1, 0, N - 1)
    print(calculate(caltree[1]))
