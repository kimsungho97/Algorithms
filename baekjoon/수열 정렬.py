n=int(input())
arr=list(map(int,input().split()))

s=sorted(arr)

p=[0 for i in range(n)]

result=[]

for i in range(n):
    for j in range(n):
        if(arr[i]==s[j]):
            result.append(j+p[j])
            p[j]+=1
            break                

for i in result:
    print(i,end=" ")