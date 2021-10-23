import sys


def bfs(board, visited, row_size, col_size, row, col):
    stack = [(row, col)]
    count = 0
    visited[row][col] = 1

    while(len(stack) > 0):
        current = stack.pop()

        # 상
        if(current[0] > 0):
            temp = (current[0]-1, current[1])
            if(board[temp[0]][temp[1]] == 1):
                if(visited[temp[0]][temp[1]] > visited[current[0]][current[1]]+1):
                    visited[temp[0]][temp[1]
                                     ] = visited[current[0]][current[1]]+1
                    stack.append(temp)
        # 하
        if(current[0] < row_size-1):
            temp = (current[0]+1, current[1])
            if(board[temp[0]][temp[1]] == 1):
                if(visited[temp[0]][temp[1]] > visited[current[0]][current[1]]+1):
                    visited[temp[0]][temp[1]
                                     ] = visited[current[0]][current[1]]+1
                    stack.append(temp)
        # 좌
        if(current[1] > 0):
            temp = (current[0], current[1]-1)
            if(board[temp[0]][temp[1]] == 1):
                if(visited[temp[0]][temp[1]] > visited[current[0]][current[1]]+1):
                    visited[temp[0]][temp[1]
                                     ] = visited[current[0]][current[1]]+1
                    stack.append(temp)
        # 우
        if(current[1] < col_size-1):
            temp = (current[0], current[1]+1)
            if(board[temp[0]][temp[1]] == 1):
                if(visited[temp[0]][temp[1]] > visited[current[0]][current[1]]+1):
                    visited[temp[0]][temp[1]
                                     ] = visited[current[0]][current[1]]+1
                    stack.append(temp)


board = []
visited = []

row_size, col_size = list(map(int, sys.stdin.readline().strip().split()))
for _ in range(row_size):
    board.append(list(map(int, list(sys.stdin.readline().strip()))))
    visited.append([row_size*col_size for i in range(col_size)])

bfs(board, visited, row_size, col_size, 0, 0)
print(visited[row_size-1][col_size-1])
