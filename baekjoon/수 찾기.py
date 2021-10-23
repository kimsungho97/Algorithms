n=int(input())
arr=list(map(int,input().split()))

m=int(input())
to_find=list(map(int,input().split()))

arr.sort()

result=[]
for i in to_find:
    if i in arr:
        result.append(1)
    else:
        result.append(0)

for i in result:
    print(i)