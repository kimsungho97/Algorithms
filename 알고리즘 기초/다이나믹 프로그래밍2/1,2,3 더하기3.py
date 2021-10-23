n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

max_num = max(arr)
dp = [0 for i in range(max_num+1)]


dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, max_num+1):
    for j in range(i-3, i):
        dp[i] += dp[j]
    if(dp[i] >= 1000000009):
        dp[i] = dp[i] % 1000000009

for i in arr:
    print(dp[i])
