n, k = list(map(int, input().split()))


def bruteforce(min_num, max_num, depth, cur_depth, record):
    if(cur_depth == depth):
        print(" ".join(list(map(str, record))))
        return
    else:
        for i in range(min_num, max_num+1):
            bruteforce(i, max_num, depth, cur_depth+1, record+[i])


bruteforce(1, n, k, 0, [])
