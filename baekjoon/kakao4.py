answer=3000
v, e= list(map(int,input().split()))

start=int(input())


route=[ [] for i in range(v)]

for i in range(e):
    a,b,c=list(map(int, input().split()))
    route[a-1].append((b-1,c))

infinity=9999999
result=[infinity for i in range(v)]
result[start-1]=0

cur=start-1
visited=[i for i in range(v)]



while len(visited)>0:
    for u,w in route[cur]:
        if result[u]>result[cur]+w:
            result[u]=result[cur]+w
    
    visited.remove(cur)

    
    minimum=infinity+1
    min_v=None

    for i in visited:
        if minimum>result[i]:
            minimum=result[i]
            min_v=i
    cur=min_v

for i in result:
    if i>=infinity:
        print("INF")
    else:
        print(i)




def brute_force(roads,trap,visited,dest,cur,result):
    
    global answer
    if cur==dest:
        if answer>result:
            answer=result
    else:
        for i in roads:
            if i[0]==cur and visited[i[1]]<3:
                if (i[1] in trap):
                    visited[i[1]]+=1
                    temp=roads.copy()
                    for j in range(len(temp)):
                        if temp[j][1]==i[1] or temp[j][0]==i[1]:
                            temp[j]=[temp[j][1],temp[j][0],temp[j][2]]
                    brute_force(temp,trap,visited,dest,i[1],result+i[2])
                    visited[i[1]]-=1
                else:
                    visited[i[1]]+=1
                    brute_force(roads,trap,visited,dest,i[1],result+i[2])
                    visited[i[1]]-=1

def solution(n, start, end, roads, traps):
    global answer
    visited=[0 for i in range(n+1)]
    visited[start]=1
    brute_force(roads,traps,visited,end,start,0)
    return answer

#print(solution(3,1,3,[[1, 2, 2], [3, 2, 3]],[2]))
#print(solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]],[2,3]))