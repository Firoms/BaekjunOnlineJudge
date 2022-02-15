# 고장난 계산기 테스트 2

import sys

strToInt = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "+": 10,
    "*": 11,
}
intToStr = {
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
    22: "+",
}


class SegmentTree:
    def __init__(self, formula) -> None:
        self.formula = "0" + formula
        self.depth = 0
        while 2**self.depth < len(formula):
            self.depth += 1

        self.lenLeaf = 2**self.depth
        self.tree = [0 for _ in range(2 ** (self.depth + 1))]

    def makeTree(self, node, left, right):
        if left == right:
            if left <= len(self.nums) - 1:
                self.tree[node] = self.formula[left]
                return self.tree[node]
            else:
                return 0

        self.tree[node] = self.makeTree(node * 2, left, (left + right) // 2)
        rightNode = self.makeTree(node * 2 + 1, (left + right) // 2 + 1, right)
        if self.tree[node][-1] == "+" or self.tree[node][-1] == "*":
            if rightNode == "+" or rightNode == "*":
                return self.tree[node]
        self.tree[node] += rightNode

        return self.tree[node]

    def query(self, node, left, right, l, r, x):
        if r < left or l > right:
            return self.tree[node]
        if left != right:
            self.tree[node] = self.query(node * 2, left, (left + right) // 2, l, r, x)
            rightNode = self.query(
                node * 2 + 1, (left + right) // 2 + 1, right, l, r, x
            )
            if self.tree[node][-1] == "+" or self.tree[node][-1] == "*":
                if rightNode == "+" or rightNode == "*":
                    return self.tree[node]
            self.tree[node] += rightNode
        else:
            self.tree[node] = intToStr[strToInt[self.tree[node]]+x]
        return self.tree[node]
            


N, Q = map(int, sys.stdin.readline().split())
formula = sys.stdin.readline().rstrip()
tree = SegmentTree(formula)
original = tree.makeTree(1, 1, tree.lenLeaf)

for _ in range(Q):
    l, r, x = map(int, sys.stdin.readline().split())
    query = tree.query(1, 1, tree.lenLeaf, l, r, x)
