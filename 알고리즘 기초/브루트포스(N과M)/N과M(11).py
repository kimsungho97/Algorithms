n, k = list(map(int, input().split()))
nums = list(set(map(int, input().split())))
nums.sort()


def bruteforce(nums, depth, index, cur_depth, record):
    if(depth == cur_depth):
        print(" ".join(list(map(str, record))))
        return
    for i in range(0, len(nums)):
        bruteforce(nums, depth, i, cur_depth+1, record+[nums[i]])


bruteforce(nums, k, -1, 0, [])
