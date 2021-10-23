n,m=list(map(int,input().split()))

arr=[]
for i in range(n):
    arr.append(list(input()))

check=False

for i in range(n):
    if check:
        break
    for j in range(m):
        if arr[i][j]=='S':
            #up
            if i!=0 and arr[i-1][j]=='W':
                check=True
                break
            #down
            if i!=n-1 and arr[i+1][j]=='W':
                check=True
                break
            #left
            if j!=0 and arr[i][j-1]=='W':
                check=True
                break
            #right
            if j!=m-1 and arr[i][j+1]=='W':
                check=True
                break

if check:
    print(0)
else:
    print(1)
    for i in arr:
        for j in i:
            if(j=='.'):
                print("D",end='')
            else:
                print(j,end='')
        print()
