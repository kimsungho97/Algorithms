def isPrime(n):
    if(n == 1):
        return False

    limit = int(n**(1/2))
    for i in range(2, limit+1):
        if(n % i == 0):
            return False

    return True


n = int(input())
arr = list(map(int, input().split()))

result = list(filter(lambda x: isPrime(x), arr))

print(len(result))
