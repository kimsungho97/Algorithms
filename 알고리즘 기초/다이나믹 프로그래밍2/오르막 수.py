n = int(input())
dp = []

for i in range(n):
    if(i == 0):
        dp.append([1 for j in range(10)])
    else:
        temp = []
        for j in range(10):
            if(j == 0):
                temp.append(dp[i-1][0] % 10007)
            else:
                temp.append((temp[j-1]+dp[i-1][j]) % 10007)
        dp.append(temp)

print(sum(dp[n-1]) % 10007)
