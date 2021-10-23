import sys
n = int(input())
amounts = []
for _ in range(n):
    amounts.append(int(sys.stdin.readline().strip()))

dp = []

for i in range(n):
    if(i == 0):
        dp.append([0, amounts[i], amounts[i]])
    else:
        count0 = max(dp[i-1])
        count1 = dp[i-1][0]+amounts[i]
        count2 = dp[i-1][1]+amounts[i]
        dp.append([count0, count1, count2])
print(max(dp[n-1]))
