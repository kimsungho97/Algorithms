n = int(input())
arr = list(map(int, input().split()))
result = []
min_num = None
max_num = None
max_num_index = None


for i in range(n-1, -1, -1):
    if(i == n-1):
        min_num = max_num = arr[i]
        max_num_index = i
        result.append(-1)
    elif(arr[i] >= max_num):
        result.append(-1)
        max_num = arr[i]
        max_num_index = i
    elif(arr[i] < min_num):
        result.append(arr[i+1])
        min_num = arr[i]
    else:
        k = -1
        for j in range(i+1, max_num_index+1):
            if(arr[i] < arr[j]):
                result.append(arr[j])
                break
            elif(arr[i] < result[k]):
                result.append(result[k])
                break
            k -= 1


for i in range(n-1, -1, -1):
    print(result[i], end=" ")
