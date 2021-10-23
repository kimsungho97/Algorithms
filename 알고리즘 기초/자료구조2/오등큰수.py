n = int(input())
arr = list(map(int, input().split()))

result = []
count = {}
for i in arr:
    if(count.get(i) == None):
        count[i] = 0
    count[i] += 1

record = set()

max_num = None
min_num = None
for i in range(n-1, -1, -1):
    if(i == n-1):
        result.append(-1)
        min_num = max_num = arr[i]
        continue
    if(count[arr[i]] >= count[max_num]):
        max_num = arr[i]
        result.append(-1)
    elif(count[arr[i]] < count[min_num]):
        min_num = arr[i]
        result.append(arr[i+1])
    else:
        k = -1
        for j in range(i+1, n):
            if(count[arr[i]] < count[arr[j]]):
                result.append(arr[j])
                break
            elif(count[arr[i]] < count[result[k]]):
                result.append(result[k])
                break
            k -= 1
    record.add(arr[i])

result = list(map(str, result))
result.reverse()
print(' '.join(result))
