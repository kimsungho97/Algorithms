n = int(input())
nums = []

for _ in range(n):
    nums.append(int(input()))


max_num = max(nums)

arr = [0 for i in range(max_num+1)]

arr[1] = 1
if(n > 1):
    arr[2] = 1
if(n > 2):
    arr[3] = 1

for i in range(1, max_num+1):
    a = i+1
    b = i+2
    c = i+3
    if(a <= max_num):
        arr[a] += arr[i]
    if(b <= max_num):
        arr[b] += arr[i]
    if(c <= max_num):
        arr[c] += arr[i]


for i in nums:
    print(arr[i])
