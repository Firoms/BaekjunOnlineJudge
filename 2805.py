# 나무 자르기
import sys
N, M = map(int, (sys.stdin.readline().rstrip()).split(" "))
tree_li = list(map(int, (sys.stdin.readline().rstrip()).split(" ")))
tree_li.append(0)
tree_li.sort(reverse=True)
tree_length = 0
last_tree = 0
trees = 0
for i in range(len(tree_li)-1):
    tree_length += (tree_li[i]-tree_li[i+1])*(i+1)
    if tree_length >= M:
        last_tree = tree_li[i+1]
        trees = i+1
        break

last_tree += (tree_length-M)//trees
print(last_tree)