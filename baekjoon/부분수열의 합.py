#https://www.acmicpc.net/problem/1182
n,m=list(map(int,input().split()))
arr=list(map(int,input().split()))

k=2**n
count=0

for i in range(1,k):
    temp=[]
    b=str(format(i,'b'))
    for j in range(0,n-len(b)):
        b='0'+b
    b=list(b)
    for j in range(len(b)):
        if(b[j]=='1'):
            temp.append(arr[j])
    if(sum(temp)==m):
        count+=1

print(count)