n = int(input())

dp = []

for i in range(n):
    if(i == 0):
        dp.append([1, 1, 1])
    else:
        left = dp[i-1][1]+dp[i-1][2]
        right = dp[i-1][0]+dp[i-1][2]
        empty = sum(dp[i-1])
        dp.append([left % 9901, right % 9901, empty % 9901])

print(sum(dp[n-1]) % 9901)
