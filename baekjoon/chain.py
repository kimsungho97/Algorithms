#https://www.acmicpc.net/problem/2785

n= int(input())

arr=sorted(list(map(int,input().split(" "))))

count=0

while True:
    if len(arr)==1:
        break
    else:
        arr[0]+=-1
        arr[-2]+=arr[-1]+1
        del arr[-1]
        count+=1
        if arr[0]==0:
            del arr[0]


print(count)


