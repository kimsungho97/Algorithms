n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))

nums.sort()


def bruteforce(nums, depth, cur_depth, record):
    if(depth == cur_depth):
        print(" ".join(list(map(str, record))))
        return
    else:
        for i in nums:
            if(not i in record):
                bruteforce(nums, depth, cur_depth+1, record+[i])


bruteforce(nums, k, 0, [])
