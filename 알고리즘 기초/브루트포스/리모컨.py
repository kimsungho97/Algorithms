channel = int(input())
n = int(input())
broken = []
if(n != 0):
    broken = list(map(int, input().split()))
nums = [i for i in range(10)]

for i in broken:
    nums.remove(i)

minimum = abs(channel-100)


def bruteforce(nums, record):
    global minimum, channel
    for i in range(len(nums)):
        temp = record+str(nums[i])
        if(len(temp) >= len(str(channel))-1):
            minimum = min(minimum, len(temp)+abs(channel-int(temp)))
        if(len(temp) <= len(str(channel))):
            bruteforce(nums, temp)


bruteforce(nums, '')

print(minimum)
