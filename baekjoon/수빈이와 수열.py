n=int(input())
arr=list(map(int,input().split()))

for i in range(len(arr)):
    arr[i]*=(i+1)

for i in range(len(arr)-1):
    arr[len(arr)-i-1]-=arr[len(arr)-i-2]

print(' '.join(list(map(str,arr))))