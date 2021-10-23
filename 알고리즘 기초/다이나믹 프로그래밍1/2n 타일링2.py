n = int(input())


arr = [0 for i in range(n+1)]


arr[1] = 1
if(n > 1):
    arr[2] = 2

for i in range(1, n+1):
    a = i+1
    b = i+2
    if(a <= n):
        arr[a] += arr[i]
    if(b <= n):
        arr[b] += arr[i]*2

print(arr[n] % 10007)
