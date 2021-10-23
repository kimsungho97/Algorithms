import sys
n = int(input())

answer = []

for _ in range(n):
    length = int(sys.stdin.readline().strip())
    price1 = list(map(int, sys.stdin.readline().strip().split()))
    price2 = list(map(int, sys.stdin.readline().strip().split()))
    dp = []
    for i in range(length):
        if(i == 0):
            dp.append([price1[i], price2[i], 0])
        else:
            dp.append([price1[i]+max(dp[i-1][1], dp[i-1][2]), price2[i] +
                      max(dp[i-1][0], dp[i-1][2]), max(dp[i-1][0], dp[i-1][1])])
    answer.append(max(dp[length-1]))

for i in answer:
    print(i)
