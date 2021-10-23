# https://www.acmicpc.net/problem/1083

n = int(input())
arr = list(map(int, input().split()))
k = int(input())

for _ in range(k):
    for index in range(n - 1):
        if arr[index] < arr[index + 1]:
            temp = arr[index + 1]
            arr[index + 1] = arr[index]
            arr[index] = temp
            break
    break

print(" ".join(list(map(str, arr))))
