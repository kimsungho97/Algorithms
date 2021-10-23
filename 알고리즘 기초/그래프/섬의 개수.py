import sys


def bfs(board, visited, row_size, col_size, row, col):
    stack = [(row, col)]
    count = 0

    while(len(stack) > 0):
        current = stack.pop()

        if(visited[current[0]][current[1]] == 1):
            continue
        count += 1
        visited[current[0]][current[1]] = 1

        up, down, left, right = False, False, False, False
        # 상
        if(current[0] > 0):
            up = True
            temp = (current[0]-1, current[1])
            if(visited[temp[0]][temp[1]] == 0 and board[temp[0]][temp[1]] == 1):
                stack.append(temp)
        # 하
        if(current[0] < row_size-1):
            down = True
            temp = (current[0]+1, current[1])
            if(visited[temp[0]][temp[1]] == 0 and board[temp[0]][temp[1]] == 1):
                stack.append(temp)
        # 좌
        if(current[1] > 0):
            left = True
            temp = (current[0], current[1]-1)
            if(visited[temp[0]][temp[1]] == 0 and board[temp[0]][temp[1]] == 1):
                stack.append(temp)
        # 우
        if(current[1] < col_size-1):
            right = True
            temp = (current[0], current[1]+1)
            if(visited[temp[0]][temp[1]] == 0 and board[temp[0]][temp[1]] == 1):
                stack.append(temp)
        # 대각선(상좌)
        if(up and left):
            temp = (current[0]-1, current[1]-1)
            if(visited[temp[0]][temp[1]] == 0 and board[temp[0]][temp[1]] == 1):
                stack.append(temp)
        # 대각선(상우)
        if(up and right):
            temp = (current[0]-1, current[1]+1)
            if(visited[temp[0]][temp[1]] == 0 and board[temp[0]][temp[1]] == 1):
                stack.append(temp)
        # 대각선(하좌)
        if(down and left):
            temp = (current[0]+1, current[1]-1)
            if(visited[temp[0]][temp[1]] == 0 and board[temp[0]][temp[1]] == 1):
                stack.append(temp)
        # 대각선(하우)
        if(down and right):
            temp = (current[0]+1, current[1]+1)
            if(visited[temp[0]][temp[1]] == 0 and board[temp[0]][temp[1]] == 1):
                stack.append(temp)

    return count


while(True):
    col_size, row_size = list(map(int, sys.stdin.readline().strip().split()))
    if(col_size == 0 and row_size == 0):
        break
    board = []
    visited = []
    for _ in range(row_size):
        board.append(list(map(int, sys.stdin.readline().strip().split())))
        visited.append([0 for i in range(col_size)])

    result = []

    for row in range(row_size):
        for col in range(col_size):
            if(board[row][col] == 0):
                continue
            elif(visited[row][col] == 1):
                continue
            else:
                result.append(
                    bfs(board, visited, row_size, col_size, row, col))

    print(len(result))
