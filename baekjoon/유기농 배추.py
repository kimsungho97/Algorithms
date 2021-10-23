#https://www.acmicpc.net/problem/1012
n=int(input())

result=[]
for _ in range(n):
    arr=[]
    group=[]

    row,col,m=list(map(int,input().split()))
    for i in range(m):
        arr.append(list(map(int,input().split())))
    
    #그룹 생성(인접한 배추의 그룹)
    for r,c in arr:
        inserted=False
        index=None
        to_remove=set()
        for i in range(len(group)):
            for j in range(len(group[i])):
                if abs(group[i][j][0]-r)==1 and  group[i][j][1]==c:
                    if inserted:
                        group[index]=group[index]+group[i].copy()
                        del group[i]
                        group.append([])
                        break
                    else:
                        group[i].append([r,c])
                        inserted=True
                        index=i
                        break
                elif abs(group[i][j][1]-c)==1 and  group[i][j][0]==r:
                    if inserted:
                        group[index]=group[index]+group[i].copy()
                        del group[i]
                        group.append([])
                        break
                    else:
                        group[i].append([r,c])
                        inserted=True
                        index=i
                        break
            
        if not inserted:
            group.append([[r,c]])
    
    to_remove=0
    for i in group:
        if(i==[]):
            to_remove+=1
    result.append(len(group)-to_remove)
    
for i in result:
    print(i)

