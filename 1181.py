# 단어 정렬
N = int(input())
word_list = []
for i in range(51):
    word_list.append([])
for i in range(N):
    word = input()
    if word not in word_list[len(word)]:
        word_list[len(word)].append(word)
for i in range(51):
    word_list[i].sort()
    for j in word_list[i]:
        print(j)