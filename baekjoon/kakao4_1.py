answer=3000
def brute_force(roads,trap,visited,dest,cur,result,is_trap):
    global answer
    if cur==dest:
        if answer>result:
            answer=result
    else:
        for i in roads[cur]:

            '''
            if i[0]==cur:
                if (i[1] in trap) and visited[i[1]]<=1:
                    visited[i[1]]+=1
                    temp=roads.copy()
                    for j in range(len(temp)):
                        if temp[j][1]==i[1] or temp[j][0]==i[1]:
                            temp[j]=[temp[j][1],temp[j][0],temp[j][2]]
                    brute_force(temp,trap,visited,dest,i[1],result+i[2])
                    visited[i[1]]-=1
                elif (i[1] not in trap) and visited[i[1]]==0:
                    visited[i[1]]+=1
                    brute_force(roads,trap,visited,dest,i[1],result+i[2])
                    visited[i[1]]-=1
            '''
                    
def solution(n, start, end, roads, traps):
    global answer
    road=[[]for i in range(n+1)]
    
    for i in roads:
        road[i[0]].append((i[1],i[2]))
    visited=[0 for i in range(n+1)]
    brute_force(road,traps,visited,end,start,0)
    return answer

#print(solution(3,1,3,[[1, 2, 2], [3, 2, 3]],[2]))
#print(solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]],[2,3]))