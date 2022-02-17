# 고장난 계산기 테스트 2

import sys
import random
sys.setrecursionlimit(10**7)
strToInt = {"0": 0,"1": 1,"2": 2,"3": 3,"4": 4,"5": 5,"6": 6,"7": 7,"8": 8,"9": 9,"+": 10,"*": 11,}
intToStr = {0: "0",1: "1",2: "2",3: "3",4: "4",5: "5",6: "6",7: "7",8: "8",9: "9",10: "+",11: "*",12: "0",13: "1",14: "2",15: "3",16: "4",17: "5",18: "6",19: "7",20: "8",21: "9",22: "+",}


class SegmentTree:
    def __init__(self, formula) -> None:
        self.formula = "0" + formula
        self.depth = 0
        while 2**self.depth < len(formula):
            self.depth += 1

        self.lenLeaf = 2**self.depth
        self.tree = ['' for _ in range(2 ** (self.depth + 1))]

    def makeTree(self, node, left, right):
        if node > len(self.tree)-1:
            return ''
        if left == right:
            if left <= len(self.formula) - 1:
                self.tree[node] = self.formula[left]
                return self.tree[node]
            else:
                return ''

        self.tree[node] = self.makeTree(node * 2, left, (left + right) // 2)
        rightNode = self.makeTree(node * 2 + 1, (left + right) // 2 + 1, right)
        if self.tree[node]:
            if self.tree[node][-1] == "+" or self.tree[node][-1] == "*":
                if rightNode:
                    if rightNode[0] == "+" or rightNode[0] == "*":
                        if len(rightNode)>1:
                            self.tree[node] += rightNode[1:]
                        return self.tree[node]

            if rightNode:
                self.tree[node] += rightNode

            return self.tree[node]

    def query(self, node, left, right, l, r, x):
        if node >len(self.tree)-1:
            return ''
        if r < left or l > right:
            return self.tree[node]
        if left != right:
            self.tree[node] = self.query(node * 2, left, (left + right) // 2, l, r, x)
            rightNode = self.query(
                node * 2 + 1, (left + right) // 2 + 1, right, l, r, x
            )
            if self.tree[node][-1] == "+" or self.tree[node][-1] == "*":
                if rightNode:
                    if rightNode[0] == "+" or rightNode[0] == "*":
                        if len(rightNode)>1:
                            self.tree[node] += rightNode[1:]
                        else:
                            return self.tree[node]
            if rightNode:
                self.tree[node] += rightNode
        else:
            self.tree[node] = intToStr[strToInt[self.tree[node]]+x]
        return self.tree[node]
            

if __name__=="__main__":
    # N, Q = map(int, sys.stdin.readline().split())
    N = random.randint(1, 100001)
    Q = 5
    # formula = sys.stdin.readline().rstrip()
    formula = [intToStr[random.randint(0, 12)] for _ in range(N)]
    formula = "".join(formula)
    tree = SegmentTree(formula)
    original = tree.makeTree(1, 1, tree.lenLeaf)
    
    if original:
        if original[0]=='+' or original[0]=='*':
            original = original[1:]
    if original:
        if original[-1]=='+'or original[-1]=='*':
            original = original[:-1]
    
    if original:
        cntPlus = original.count("+")
        cntMult = original.count("*")
        original = original.replace("+", "\")+int(\"", cntPlus)
        original = original.replace("*", "\")*int(\"", cntMult)
        original = "(int(\"" + original + "\"))"
        print(eval(original)%(10**9+7))
    else:
        print(-1)

    for _ in range(Q):
        # l, r, x = map(int, sys.stdin.readline().split())
        l = random.randint(1, N+1)
        r = random.randint(l, N+1)
        x = random.randint(1, 12)
        query = tree.query(1, 1, tree.lenLeaf, l, r, x)

        if query:
            if query[0]=='+'or query[0]=='*':
                query = query[1:]
        if query:
            if query[-1]=='+'or query[-1]=='*':
                query = query[:-1]

        if query:
            cntPlus = query.count("+")
            cntMult = query.count("*")
            query = query.replace("+", "\")+int(\"", cntPlus)
            query = query.replace("*", "\")*int(\"", cntMult)
            query = "(int(\"" + query + "\"))"
            print(query)
            print(eval(query)%(10**9+7))
        else:
            print(-1)
        