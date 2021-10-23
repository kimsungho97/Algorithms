n,m=list(map(int,input().split()))

arr=[]
for i in range(n):
    arr.append(int(input()))

index=0
called=[]
result=0
while True:
    
    if index in called:
        print(-1)
        break
    called.append(index)
    index=arr[index]
    result+=1
    if index==m:
        print(result)
        break


