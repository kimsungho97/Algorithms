#https://www.acmicpc.net/problem/1018
#미완성
[row,col]=list(map(int,input().split()))

board=list()

for i in range(row):
    board.append(list(input()))

board1=list()
board2=list()

for i in range(row):
    k=list()
    for j in range(col):
        if i%2==1 and j%2==0:
            k.append('W')
        elif i%2==0 and j%2==1:
            k.append('W')
        else:
            k.append('B')
    board1.append(k)


for i in range(row):
    k=list()
    for j in range(col):
        if i%2==1 and j%2==0:
            k.append('B')
        elif i%2==0 and j%2==1:
            k.append('B')
        else:
            k.append('W')
    board2.append(k)


count1=0
count2=0
print()
for i in range(row):
    for j in range(col):
        print(board2[i][j],end="")
        if board[i][j]!=board1[i][j]:
            count1+=1
        if board[i][j]!=board2[i][j]:
            count2+=1
    print()

print((count1,count2))
                        


    