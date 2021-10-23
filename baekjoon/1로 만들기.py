k=int(input())

arr=[k for i in range(k+1)]
arr[k]=0

for i in range(k,0,-1):
    arr[i-1]=min(arr[i]+1,arr[i-1])
    if i%2==0:
        arr[int(i/2)]=min(arr[int(i/2)],arr[i]+1)
    if i%3==0:
        arr[int(i/3)]=min(arr[int(i/3)],arr[i]+1)

print(arr[1])