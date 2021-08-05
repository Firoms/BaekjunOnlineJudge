# 단어의 개수
import sys
sentence = sys.stdin.readline().strip()
if sentence != "":
    wordList = sentence.split(" ")
else:
    wordList = []
print(len(wordList))
