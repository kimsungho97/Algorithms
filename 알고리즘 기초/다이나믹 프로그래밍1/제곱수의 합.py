n = int(input())

arr = [0 for i in range(n+1)]


for i in range(int(n**(1/2))+1):
    arr[i*i] = 1

for i in range(2, n+1):
    if(arr[i] == 1):
        continue
    for j in range(1, int(i/2)+1):
        if(arr[i] == 0):
            arr[i] = arr[j]+arr[i-j]
        else:
            arr[i] = min(arr[i], arr[j]+arr[i-j])
# print(arr)
print(arr[n])
