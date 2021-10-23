# https://www.acmicpc.net/problem/2178
# DFS 미로찾기 - 항상 찾을 수 있는경우만 출력





'''
result = 0
arr = []
cost = []


def bfs(current_r, current_c, end_r, end_c, arr, count):
    global result
    global cost
    #print(current_r, current_c, count)
    count += 1
    cost[current_r][current_c] = count
    # 미로탐색 종료조건
    if current_r == end_r and current_c == end_c:
        if result > count:
            result = count
    else:
        # visited
        arr[current_r][current_c] = '0'
        # bfs 탐색
        # 왼쪽
        if current_c > 0 and arr[current_r][current_c - 1] == '1' and cost[current_r][current_c - 1] > count+1:
            bfs(current_r, current_c - 1, end_r, end_c, arr, count)
        # 오른쪽
        if current_c < end_c and arr[current_r][current_c + 1] == '1' and cost[current_r][current_c + 1] > count+1:
            bfs(current_r, current_c + 1, end_r, end_c, arr, count)
        # 위
        if current_r > 0 and arr[current_r - 1][current_c] == '1' and cost[current_r-1][current_c] > count+1:
            bfs(current_r - 1, current_c, end_r, end_c, arr, count)
        # 아래
        if current_r < end_r and arr[current_r + 1][current_c] == '1' and cost[current_r+1][current_c] > count+1:
            bfs(current_r + 1, current_c, end_r, end_c, arr, count)
        arr[current_r][current_c] = '1'


n, m = list(map(int, input().split()))

for i in range(n):
    arr.append(list(input()))
    cost.append([-1 for i in range(m)])

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == '1':
            cost[i][j] = n*m+1

result = n * m
bfs(0, 0, n-1, m-1, arr, 0)
# print(arr)
print(result)
'''