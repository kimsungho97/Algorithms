n=int(input())
arr=list(map(int,input().split()))


count=[n+1 for i in range(n)]
count[0]=0

for i in range(n):
    dest=arr[i]+i
    for j in range(min(dest+1,n)):
        count[j]=min(count[j],count[i]+1)

if(count[n-1]>=n+1):
    print(-1)
else:
    print(count[n-1])
