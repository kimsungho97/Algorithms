import sys

n = int(input())

graph = dict()


is_sunhwan = [False for i in range(n+1)]
distance = [3001 for i in range(n+1)]

for i in range(1, n+1):
    graph[i] = []

for i in range(n):
    a, b = list(map(int, sys.stdin.readline().strip().split()))
    graph[a].append(b)
    graph[b].append(a)


def dfs(graph, visited, current, start, before, distance_from):
    global is_sunhwan, distance

    to_visit = graph[current]
    for next in to_visit:
        if(next == before):
            continue
        elif(next in visited):
            if(visited.index(next) == 0):
                distance[start] = 0
            else:
                distance[start] = min(distance[start], visited.index(next))
        elif next not in visited and distance[next] == 3001:
            dfs(graph, visited+[next], next,
                start, current, distance_from+1)


for i in range(1, n+1):
    dfs(graph, [i], i, i, -1, 1)


for i in range(1, n+1):
    if(is_sunhwan[i] == True):
        print(0, end=" ")
    else:
        print(distance[i], end=" ")
