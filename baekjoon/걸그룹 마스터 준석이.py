n,m=list(map(int,input().split()))

groups={}
result=[]

for i in range(n):
    name=input()
    num=int(input())
    groups[name]=[]
    for j in range(num):
        groups[name].append(input())
    groups[name]=sorted(groups[name])


for i in range(m):
    name=input()
    kind=int(input())
    if kind==0:
        for j in groups[name]:
            result.append(j)
    elif kind==1:
        for j in groups.keys():
            if name in groups[j]:
                result.append(j)
                break

for i in result:
    print(i)