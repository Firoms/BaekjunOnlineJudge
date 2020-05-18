sent = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'
alpha = list(alpha)
for i in alpha :
    cnt = sent.count(i)
    print(cnt, end =" ")