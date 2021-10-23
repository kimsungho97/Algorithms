n, k = list(map(int, input().split()))


def bruteforce(max_num, depth, record, cur_depth):
    if(depth == cur_depth):
        print(" ".join(list(map(str, record))))
        return
    else:
        for i in range(1, max_num+1):
            if(not i in record):
                bruteforce(max_num, depth, record+[i], cur_depth+1)


bruteforce(n, k, [], 0)
