row, col = list(map(int, input().split()))

board = []
visited = []
groups = []
for i in range(row):
    board.append(list(map(int, input().split())))
    visited.append([0 for j in range(col)])

queue = [(0, 0)]
result = 0

while len(queue) > 0:
    cur = queue[0]
    del queue[0]
    visited[cur[0]][cur[1]] = 1
    
    

    if board[cur[0]][cur[1]] != 0:
        is_connnected = False
        for group in groups:
            if abs(group[0] - cur[0]) + abs(group[1] - cur[1]) < 2:
                is_connnected = True
                break

        if not is_connnected:
            result += 1

        if cur[0] < row - 1 and visited[cur[0]+1][cur[1]]==0:
            queue.append((cur[0] + 1, cur[1]))
        if cur[1] < col - 1 and visited[cur[0]][cur[1]+1] == 0:
            queue.append((cur[0], cur[1] + 1))
        
    
print(len(groups))
