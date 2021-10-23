# https://www.acmicpc.net/problem/1260

'''
입력
4 5 1
1 2
1 3
1 4
2 4
3 4

출력
1 2 4 3
1 2 3 4
'''


def dfs(graph, visited, cur, record):
    if graph.get(cur) == None:
        return [cur]
    visited[cur] = 1

    count = 0
    for i in sorted(graph[cur]):
        if visited[i] == 0:
            count += 1
            record = dfs(graph, visited, i, record+[i])

    return record


def bfs(graph, visited, cur):
    if graph.get(cur) == None:
        return [cur]
    queue = [cur]
    visited.append(queue[0])
    num_node = len(list(graph.keys()))
    while len(visited) < num_node and len(queue) != 0:
        search = queue[0]
        del queue[0]
        for i in sorted(graph[search]):
            if i not in visited:
                queue.append(i)
                visited.append(i)
    return visited


# n-> 정점 개수
# m-> 간선 개수
# start -> 시작점
n, m, start = list(map(int, input().split()))
start -= 1
graph = {}

for i in range(m):
    vertex1, vertex2 = list(map(int, input().split()))
    vertex1 -= 1
    vertex2 -= 1
    if graph.get(vertex1) == None:
        graph[vertex1] = []
    if graph.get(vertex2) == None:
        graph[vertex2] = []
    graph[vertex1].append(vertex2)
    graph[vertex2].append(vertex1)

visited_dfs = [0 for i in range(n)]
visited_bfs = []

dfs_result = dfs(graph, visited_dfs, start, [start])
bfs_result = bfs(graph, visited_bfs, start)

for i in range(len(dfs_result)):
    dfs_result[i] += 1

for i in range(len(bfs_result)):
    bfs_result[i] += 1

print(" ".join(list(map(str, dfs_result))))
print(" ".join(list(map(str, bfs_result))))
