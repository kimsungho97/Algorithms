import sys


n, m = list(map(int, sys.stdin.readline().strip().split()))

relations = {}

for _ in range(m):
    a, b = list(map(int, sys.stdin.readline().strip().split()))
    if(relations.get(a) == None):
        relations[a] = []
    if(relations.get(b) == None):
        relations[b] = []

    relations[a].append(b)
    relations[b].append(a)

nodes = [1 for i in range(n+2)]
count = 0


def bfs(relations, current):
    global nodes

    stack = [current]
    while(len(stack) != 0):
        cur_node = stack.pop()

        if(nodes[cur_node] == 0):
            continue
        nodes[cur_node] = 0
        if(relations.get(cur_node) == None):
            continue
        for node in sorted(relations[cur_node]):
            if(nodes[node] == 1):
                stack.append(node)


for i in range(1, n+1):
    if(nodes[i] == 1):
        count += 1
        bfs(relations, i)


print(count)
