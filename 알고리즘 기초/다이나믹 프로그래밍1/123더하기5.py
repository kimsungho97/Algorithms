n = int(input())
nums = []

for _ in range(n):
    nums.append(int(input()))


max_num = max(nums)

arr = [[0, 0, 0, 0] for i in range(max_num+1)]

arr[1] = [0, 1, 0, 0]
if(max_num > 1):
    arr[2] = [0, 0, 1, 0]
if(max_num > 2):
    arr[3] = [0, 1, 1, 1]


def dp(n):
    global arr, max_num
    if(n > max_num):
        return
    arr[n][1] += arr[n-1][2]+arr[n-1][3]
    arr[n][2] += arr[n-2][1]+arr[n-2][3]
    arr[n][3] += arr[n-3][1]+arr[n-3][2]
    arr[n] = list(map(lambda x: x % 1000000009, arr[n]))


for i in range(4, max_num+1):
    dp(i)

for i in nums:
    print((arr[i][1]+arr[i][2]+arr[i][3]) % 1000000009)
