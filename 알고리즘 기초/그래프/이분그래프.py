import sys

k = int(input())

for _ in range(k):
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

    color = [0 for i in range(n+2)]

    def bfs(relations, current):
        global color

        stack = [current]
        while(len(stack) != 0):
            cur_node = stack.pop()

            if(color[cur_node] == 0):
                color[cur_node] = 1

            if(relations.get(cur_node) == None):
                continue
            for node in sorted(relations[cur_node]):
                if(color[node] == 0):
                    stack.append(node)
                    color[node] = -color[cur_node]
                elif(color[node] == color[cur_node]):
                    return False
        return True

    result = True
    for i in range(1, n+1):
        if(color[i] == 0):
            result = result and bfs(relations, i)
        if(result == False):
            break

    if(result):
        print("YES")
    else:
        print("NO")
    # print(count)
