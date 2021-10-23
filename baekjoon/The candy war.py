#https://www.acmicpc.net/problem/9037

def same_candy(arr):
    temp=arr[0]
    for i in arr:
        if temp!=i:
            return False
    return True

n=int(input())
result=[]
for _ in range(n):
    k=int(input())
    arr=list(map(int,input().split()))
    cur=0
    for i in range(len(arr)):
        if arr[i]%2==1:
            arr[i]+=1
    while not same_candy(arr):
        temp=arr.copy()
        for i in range(len(temp)):
            temp[i]=int(temp[i]/2)
        for i in range(len(arr)):
            arr[(i+1)%k]=temp[i]+arr[(i+1)%k]
            arr[i]-=temp[i]
        for i in range(len(arr)):
            if arr[i]%2==1:
                arr[i]+=1
        cur+=1

    result.append(cur)

for i in result:
    print(i)
