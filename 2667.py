# 단지번호붙이기



def num_homes(home): 
    def checkupdownleftright(x, y, num):
        if x<=-1 or x>=len(home[0]) or y<=-1 or y>=len(home):
            return
        if home[y][x]=='1':
            home[y][x]= num
        else:
            return

        checkupdownleftright(x-1, y, num)
        checkupdownleftright(x+1, y, num)
        checkupdownleftright(x, y-1, num)
        checkupdownleftright(x, y+1, num)

    homenum = 0
    for rownum in range(len(home)):
        for onehomenum in range(len(home[rownum])):
            if home[rownum][onehomenum]=='1':
                homenum +=1
                checkupdownleftright(onehomenum, rownum, homenum)
    print(homenum)
    count = []
    for num in range(1, homenum+1):
        num_count = 0
        for j in homes:
            num_count += j.count(num)
        count.append(num_count)
    count.sort()
    for i in count:
        print(i)
        


N = int(input())
homes = []
for i in range(N):
    a = input()
    li = []
    for j in a:
        li.append(j)
    homes.append(li)
num_homes(homes)