n, k = list(map(int, input().split()))

result = [[0 for i in range(n+1)] for j in range(k+1)]

for i in range(n+1):
    result[1][i] = 1

for i in range(2, k+1):
    for j in range(0, n+1):
        for col in range(0, j+1):
            result[i][j] += result[i-1][j-col]

# for i in result:
#    print(i)
print(result[k][n] % 1000000000)
