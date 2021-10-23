n = int(input())
nums = list(map(int, input().split()))

results = list(map(lambda x: [x, x], nums))
for i in range(1, len(results)):
    results[i][0] = max(nums[i], results[i][0] +
                        results[i-1][0])
    results[i][1] = max(results[i-1][0],
                        nums[i]+results[i-1][1])

max_num = -999999999999
for result in results:
    max_num = max(max_num, result[0], result[1])

print(max_num)
