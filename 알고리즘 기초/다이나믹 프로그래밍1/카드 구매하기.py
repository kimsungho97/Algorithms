n = int(input())


prices = [0]
prices.extend(list(map(int, input().split())))

result = [0 for i in range(n+1)]

for i in range(1, n+1):

    result[i] = prices[i]

    for j in range(1, int(i/2)+1):
        result[i] = max(result[i], result[i-j]+prices[j])
# print(result)
print(result[n])
