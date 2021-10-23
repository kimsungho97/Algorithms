n = int(input())


arr = [n for i in range(n+1)]

for i in range(1, n+1):
    if(i == 1):
        arr[i] = 0

    a = i+1
    b = i*2
    c = i*3
    if(a <= n and arr[a] > arr[i]):
        arr[a] = arr[i]+1
    if(b <= n and arr[b] > arr[i]):
        arr[b] = arr[i]+1
    if(c <= n and arr[c] > arr[i]):
        arr[c] = arr[i]+1

print(arr[n])
