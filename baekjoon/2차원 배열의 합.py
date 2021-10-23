#https://www.acmicpc.net/problem/2167

n,m=list(map(int,input().split()))

arr=[]
add_index=[]
result=[]

for i in range(n):
    arr.append(list(map(int,input().split())))

k=int(input())
for i in range(k):
    add_index.append(list(map(int,input().split())))
    for j in range(4):
        add_index[i][j]-=1

for i in add_index:
    temp=0
    for j in range(i[0],i[2]+1):
        for k in range(i[1],i[3]+1):
            temp+=arr[j][k]
    result.append(temp)

for i in result:
    print(i)


