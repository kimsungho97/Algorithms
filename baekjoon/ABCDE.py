num_human,k=list(map(int,input().split()))

relations=[[] for i in range(num_human)]
is_friend=False

for i in range(k):
    a,b=list(map(int,input().split()))
    relations[a].append(b)
    relations[b].append(a)

def dfs(num_human,k,relations,visited,now):
    if(sum(visited)>=5):
        print(1)
        quit()
    if(sum(visited)==0) and now==-1:
        for i in range(num_human):
            dfs(num_human,k,relations,visited,i)
    elif now==0:
        return
    else:
        temp=visited.copy()
        current=now
        temp[current]=1

        for i in relations[current]:
            if visited[i]==0:
                dfs(num_human,k,relations,temp,i)
                
            
        
            


visited=[0 for i in range(num_human)]
dfs(num_human,k,relations,visited,-1)


print(0)




