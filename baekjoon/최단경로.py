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



