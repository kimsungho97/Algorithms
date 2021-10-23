def countRow(n, candy, row, col, origin):
    count = 1
    temp_col = col-1
    while(temp_col >= 0 and candy[row][temp_col] == origin):
        count += 1
        temp_col -= 1
    temp_col = col+1
    while(temp_col < n and candy[row][temp_col] == origin):
        count += 1
        temp_col += 1
    return count


def countCol(n, candy, row, col, origin):
    count = 1
    temp_row = row-1
    while(temp_row >= 0 and candy[temp_row][col] == origin):
        count += 1
        temp_row -= 1
    temp_row = row+1
    while(temp_row < n and candy[temp_row][col] == origin):
        count += 1
        temp_row += 1
    return count


n = int(input())

candy = []
for i in range(n):
    candy.append(list(input()))


result = 0
for i in range(n):
    for j in range(n):
        result = max(result, countRow(n, candy, i, j, candy[i][j]))
        result = max(result, countCol(n, candy, i, j, candy[i][j]))
        if(result == n):
            print(result)
            exit(0)

for i in range(n):
    for j in range(n):
        origin = candy[i][j]
        # row change
        if(i != 0 and candy[i-1][j] != origin):
            candy[i][j] = candy[i-1][j]
            candy[i-1][j] = origin
            result = max(result, countRow(n, candy, i, j, candy[i][j]))
            result = max(result, countCol(n, candy, i, j, candy[i][j]))
            candy[i-1][j] = candy[i][j]
            candy[i][j] = origin

        if(i != n-1 and candy[i+1][j] != origin):
            candy[i][j] = candy[i+1][j]
            candy[i+1][j] = origin
            result = max(result, countRow(n, candy, i, j, candy[i][j]))
            result = max(result, countCol(n, candy, i, j, candy[i][j]))
            candy[i+1][j] = candy[i][j]
            candy[i][j] = origin

        # col change
        if(j != 0 and candy[i][j-1] != origin):
            candy[i][j] = candy[i][j-1]
            candy[i][j-1] = origin
            result = max(result, countRow(n, candy, i, j, candy[i][j]))
            result = max(result, countCol(n, candy, i, j, candy[i][j]))
            candy[i][j-1] = candy[i][j]
            candy[i][j] = origin

        if(j != n-1 and candy[i][j+1] != origin):
            candy[i][j] = candy[i][j+1]
            candy[i][j+1] = origin
            result = max(result, countRow(n, candy, i, j, candy[i][j]))
            result = max(result, countCol(n, candy, i, j, candy[i][j]))
            candy[i][j+1] = candy[i][j]
            candy[i][j] = origin

        if(result == n):
            print(result)
            exit(0)


print(result)
