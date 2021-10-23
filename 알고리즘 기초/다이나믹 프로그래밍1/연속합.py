n = int(input())
nums = list(map(int, input().split()))

results = nums[:]
for i in range(1, len(results)):
    results[i] = max(results[i], results[i]+results[i-1])

print(max(results))
