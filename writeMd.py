import os

algorithmTypes = {
    "Level1": "난이도 ★",
    "Level2": "난이도 ★★",
    "Level3": "난이도 ★★★",
    "Special": "번외 문제",
}
markdownFile = open(f"./README.md", "w", encoding="UTF-8")
markdownFile.write(
    "Python을 이용한 백준 온라인 저지 사이트 문제풀이 내용입니다.   \nhttps://www.acmicpc.net/   \n"
)
for algorithmType in algorithmTypes.keys():
    markdownFile.write(f"\n#### {algorithmTypes[algorithmType]}\n")
    files = os.listdir(f"./{algorithmType}")

    file_list = []

    for file in files:
        pythonFile = open(f"./{algorithmType}/{file}", "r", encoding="UTF-8")
        title = pythonFile.readline()[2:-1]
        filenum = file.split(".")[0]
        file_list.append([int(filenum), title, file])
    file_list.sort()

    for filenum, title, file in file_list:
        markdownFile.write(f"- [{filenum}번 : {title}](./{algorithmType}/{file})    \n")
markdownFile.close()
