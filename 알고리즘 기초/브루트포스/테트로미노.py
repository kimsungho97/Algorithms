def get_location(src, vec):
    temp = src.copy()
    temp[0] += vec[0]
    temp[1] += vec[1]
    return temp


def calc_sum(board, tetris, row, col):
    result = 0
    for r, c in tetris:
        temp_r = row+r
        temp_c = col+c
        result += board[temp_r][temp_c]
    return result


row, col = map(int, input().split())
board = []
for i in range(row):
    board.append(list(map(int, input().split())))


maximum = 0


# 하나의 블록으로 부터 4가지 방향으로 3회 뻗어나가 생성될 수 있음
left, right, up, down = 0, 1, 2, 3
direction = {left: [0, -1], right: [0, 1], up: [1, 0], down: [-1, 0]}
tetris = [[0, 0]]

# 모든 테트리스 모양별로 반복
for i in range(0, 4):
    tetris = [[0, 0]]
    tetris.append(get_location(tetris[0], direction[i]))

    for j in range(0, 4):
        tetris = tetris[:2]
        temp_loc = get_location(tetris[1], direction[j])

        if temp_loc in tetris:
            continue
        else:
            tetris.append(temp_loc)

        for k in range(0, 4):
            tetris = tetris[:3]
            temp_loc = get_location(tetris[2], direction[k])

            if temp_loc in tetris:
                continue
            else:
                tetris.append(temp_loc)

            result = 0
            ll = abs(min(list(map(lambda x: x[1], tetris))))
            rr = abs(max(list(map(lambda x: x[1], tetris))))
            uu = abs(max(list(map(lambda x: x[0], tetris))))
            dd = abs(min(list(map(lambda x: x[0], tetris))))

            for r in range(dd, row-uu):
                for c in range(ll, col-rr):
                    result = calc_sum(board, tetris, r, c)
                    if maximum < result:
                        maximum = result

# 빠진 모양 계산
tetris = [[0, 0]]+list(direction.values())

for i in tetris[1:]:
    temp = tetris.copy()
    temp.remove(i)
    result = 0
    ll = abs(min(list(map(lambda x: x[1], temp))))
    rr = abs(max(list(map(lambda x: x[1], temp))))
    uu = abs(max(list(map(lambda x: x[0], temp))))
    dd = abs(min(list(map(lambda x: x[0], temp))))

    for r in range(dd, row-uu):
        for c in range(ll, col-rr):
            result = calc_sum(board, temp, r, c)
            if maximum < result:
                maximum = result

print(maximum)
