# 카드 게임
import sys

card_li = []
for _ in range(5):
    card_li.append(int(sys.stdin.readline()))
print(sum(card_li))
