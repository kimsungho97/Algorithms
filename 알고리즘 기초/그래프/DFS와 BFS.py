n, m, start = list(map(int, input().split()))

relations = {}
for i in range(m):
    a, b = list(map(int, input().split()))
    if(relations.get(a) == None):
        relations[a] = []
    if(relations.get(b) == None):
        relations[b] = []

    relations[a].append(b)
    relations[b].append(a)


result = [start]


def dfs(relations, current):
    global result

    if(relations.get(current) == None):
        return
    for i in sorted(relations[current]):
        if(i == current or i in result):
            continue
        result.append(i)
        dfs(relations, i)


dfs(relations, start)
print(" ".join(list(map(str, result))))


result = []


def bfs(relations, current):
    global result

    stack = [current]
    while(len(stack) != 0):
        cur_node = stack[0]
        stack.remove(cur_node)
        if(cur_node in result):
            continue
        result.append(cur_node)
        if(relations.get(cur_node) == None):
            continue
        for node in sorted(relations[cur_node]):
            if(not node in result):
                stack.append(node)


bfs(relations, start)

print(" ".join(list(map(str, result))))
