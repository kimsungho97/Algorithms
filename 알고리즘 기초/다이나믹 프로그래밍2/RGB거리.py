import sys
n = int(input())

prices = []
for i in range(n):
    prices.append(list(map(int, sys.stdin.readline().strip().split())))

dp = []
for i in range(n):
    if(i == 0):
        dp.append(prices[i])
    else:
        red = prices[i][0]+min(dp[i-1][1], dp[i-1][2])
        green = prices[i][1]+min(dp[i-1][0], dp[i-1][2])
        blue = prices[i][2]+min(dp[i-1][0], dp[i-1][1])
        dp.append([red, green, blue])

print(min(dp[n-1]))
