#https://www.acmicpc.net/problem/16507

n,m,c=list(map(int,input().split()))
quiz=[]
arr=[]

for i in range(n):
    arr.append(list(map(int,input().split())))
    #row별로 누적합 생성
    for j in range(1,m):
        arr[i][j]+=arr[i][j-1]

for i in range(c):
    quiz.append(list(map(int,input().split())))

result=[]
for i in quiz:
    temp=0
    count=(i[2]-i[0]+1)*(i[3]-i[1]+1)
    
    for r in range(i[0]-1,i[2]):
        if(i[1]==1):
            temp+=arr[r][i[3]-1]
        else:
            temp+=arr[r][i[3]-1]-arr[r][i[1]-2]
    result.append(temp/count)

for i in result:
    print(int(i))
