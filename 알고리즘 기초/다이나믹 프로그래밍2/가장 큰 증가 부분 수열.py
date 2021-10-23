n = int(input())
nums = list(map(int, input().split()))


arr = [nums[i] for i in range(n)]
path = [i for i in range(n)]

for i in range(n):
    for j in range(i):
        if(nums[j] < nums[i]):
            if(arr[i] < arr[j]+nums[i]):
                arr[i] = arr[j]+nums[i]
                path[i] = j

result = max(arr)
print(result)
'''
current = n
for i in range(n-1, -1, -1):
    if(result == arr[i]):
        current = i
        break


resultPath = []
while(True):
    resultPath.append(str(nums[current]))
    if(current == path[current]):
        break
    current = path[current]
resultPath.reverse()

print(result)
print(" ".join(resultPath))
'''
