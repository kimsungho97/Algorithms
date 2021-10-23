row, col = list(map(int, input().split()))

board = []
for r in range(row):
    board.append(list(input()))

left = [0, -1]
right = [0, 1]
up = [-1, 0]
down = [1, 0]


def move(direction, r, c):
    global row, col

    result = [r+direction[0], c+direction[1]]
    if(result[0] >= 0 and result[0] <= row-1 and result[1] >= 0 and result[1] <= col-1):
        return result
    else:
        return None


result = False
visited = set()


def dfs(board, r, c, cur_r, cur_c, color, from_r, from_c):
    global left, right, up, down, result, visited
    visited.add((cur_r, cur_c))

    moves = [move(up, cur_r, cur_c), move(down, cur_r, cur_c),
             move(left, cur_r, cur_c), move(right, cur_r, cur_c)]

    for moving in moves:
        if(moving == None):
            continue
        if(from_r != r or from_c != c):
            if(moving[0] == r and moving[1] == c):
                result = True
                return
        if(board[moving[0]][moving[1]] != color):
            continue
        board[moving[0]][moving[1]] = ''
        dfs(board, r, c, moving[0], moving[1], color, cur_r, cur_c)
        board[moving[0]][moving[1]] = color


for r in range(row):
    for c in range(col):

        color = board[r][c]
        board[r][c] = ''
        dfs(board, r, c, r, c, color, -1, -1)
        board[r][c] = color
        if(result == True):
            print("Yes")
            exit()

print('No')
