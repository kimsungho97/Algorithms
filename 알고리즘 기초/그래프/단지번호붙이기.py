import sys

k = int(input())
board = []
visited = []
for _ in range(k):
    board.append(list(map(int, list(sys.stdin.readline().strip()))))
    visited.append([0 for i in range(k)])


def bfs(board, visited, size, row, col):
    stack = [(row, col)]
    count = 0

    while(len(stack) > 0):
        current = stack.pop()

        if(visited[current[0]][current[1]] == 1):
            continue
        count += 1
        visited[current[0]][current[1]] = 1
        # 상
        if(current[0] > 0):
            temp = (current[0]-1, current[1])
            if(visited[temp[0]][temp[1]] == 0 and board[temp[0]][temp[1]] == 1):
                stack.append(temp)
        # 하
        if(current[0] < k-1):
            temp = (current[0]+1, current[1])
            if(visited[temp[0]][temp[1]] == 0 and board[temp[0]][temp[1]] == 1):
                stack.append(temp)
        # 좌
        if(current[1] > 0):
            temp = (current[0], current[1]-1)
            if(visited[temp[0]][temp[1]] == 0 and board[temp[0]][temp[1]] == 1):
                stack.append(temp)
        # 우
        if(current[1] < k-1):
            temp = (current[0], current[1]+1)
            if(visited[temp[0]][temp[1]] == 0 and board[temp[0]][temp[1]] == 1):
                stack.append(temp)
    return count


result = []

for row in range(k):
    for col in range(k):
        if(board[row][col] == 0):
            continue
        elif(visited[row][col] == 1):
            continue
        else:
            result.append(bfs(board, visited, k, row, col))

result.sort()
print(len(result))
for ans in result:
    print(ans)
