n = int(input())


arr = [[0 for i in range(10)] for j in range(n+1)]

arr[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, n+1):
    for j in range(10):
        if(j == 0):
            arr[i][j+1] += arr[i-1][j]
        elif(j == 9):
            arr[i][j-1] += arr[i-1][j]
        else:
            arr[i][j+1] += arr[i-1][j]
            arr[i][j-1] += arr[i-1][j]

print(sum(arr[n]) % 1000000000)
