n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))
nums.sort()


def bruteforce(nums, depth, cur_index, cur_depth, record):
    if(depth == cur_depth):
        print(" ".join(list(map(str, record))))
        return
    else:
        for i in range(cur_index, len(nums)):
            bruteforce(nums, depth, i, cur_depth+1, record+[nums[i]])


bruteforce(nums, k, 0, 0, [])
