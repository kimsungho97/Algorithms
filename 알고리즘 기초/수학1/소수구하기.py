def isPrime(n):
    if(n == 1):
        return False

    limit = int(n**(1/2))
    for i in range(2, limit+1):
        if(n % i == 0):
            return False

    return True


a, b = list(map(int, input().split()))

for n in range(a, b+1):
    if(isPrime(n)):
        print(n)
