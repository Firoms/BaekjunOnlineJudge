import string

a = input()
li = [i for i in string.ascii_uppercase]
re_li = []
for i in a:
    re_li.append(i.upper())
dic_li = []
for i in li:
    dic_li.append(re_li.count(i))

result = li[dic_li.index(max(dic_li))]
dic_li.sort()
if dic_li[-1] == dic_li[-2]:
    print("?")
else:
    print(result)
