n = int(input())

for _ in range(n):
    M, N, x, y = list(map(int, input().split()))
    if(M == x and N == y):
        print(M*N)
    else:
        result = -1
        if(M > N):
            M, N = N, M
            x, y = y, x

        for i in range(N+1):
            temp = i*M+x
            if(temp % N == y):
                result = i*M+x
                break
            elif(temp % N == 0 and N == y):
                result = i*M+x
                break
        print(result)
