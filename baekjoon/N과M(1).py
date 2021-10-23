#https://www.acmicpc.net/problem/15649

[m,n]=list(map(int,input().split(" ")))


nums=[i for i in range(1,m+1)]

arr=[[i] for i in nums]
max=1

while max<n:
    i=0
    while(i<len(arr)):
        if len(arr[i])==max:
            break
        else:
            del arr[i]

    
    for i in arr[:]:
        temp=sorted(list(set(nums)-set(i)))
        for j in temp:  
            if max<len(i+[j]): max=len(i+[j])
            arr.append(i+[j])

i=0
while(i<len(arr)):
    if len(arr[i])==n:
        break
    else:
        del arr[i]

        

for i in arr:
    print(" ".join(list(map(str,i))))