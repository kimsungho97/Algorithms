n, k = list(map(int, input().split()))


def bruteforce(max_num, depth, current, cur_depth, record):
    if(cur_depth == depth):
        print(" ".join(list(map(str, record))))
        return
    else:
        for i in range(current+1, max_num+1):
            bruteforce(max_num, depth, i, cur_depth+1, record+[i])


bruteforce(n, k, 0, 0, [])
