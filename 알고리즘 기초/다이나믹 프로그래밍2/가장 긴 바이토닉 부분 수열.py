n = int(input())
nums = list(map(int, input().split()))


arr = [[1, 1] for i in range(n)]
path = [i for i in range(n)]

for i in range(n):
    for j in range(i):
        if(nums[j] < nums[i]):
            if(arr[i][0] < arr[j][0]+1):
                arr[i][0] = arr[j][0]+1
                path[i] = j
        elif(nums[j] > nums[i]):
            if(arr[i][1] < arr[j][1]+1):
                arr[i][1] = arr[j][1]+1
                path[i] = j
            if(arr[i][1] < arr[j][0]+1):
                arr[i][1] = arr[j][0]+1
                path[i] = j


result1 = max(list(map(lambda x: x[0], arr)))
result2 = max(list(map(lambda x: x[1], arr)))
print(max(result1, result2))
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
