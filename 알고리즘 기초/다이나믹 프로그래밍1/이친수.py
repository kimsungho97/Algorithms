n = int(input())


arr = [[0, 0] for i in range(n+1)]

arr[1] = [0, 1]
for i in range(2, n+1):
    arr[i][0] += sum(arr[i-1])
    arr[i][1] += arr[i-1][0]

print(sum(arr[n]))
