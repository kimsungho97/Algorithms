# 에라토스테네스의 체
def Eratosthenes(n):
    arr = [True for i in range(0, n+1)]
    limit = int(n**(1/2))
    arr[0] = False
    arr[1] = False
    for i in range(2, limit+1):
        if(not arr[i]):
            continue
        else:
            k = i+i
            while(k < len(arr)):
                arr[k] = False
                k += i
    return arr


numbers = Eratosthenes(1000000)

while(True):
    n = int(input())
    if(n == 0):
        break
    else:
        result = False
        for i in range(2, int(n/2)+1):
            if(numbers[i] and numbers[n-i]):
                print(n, "=", i, "+", n-i)
                result = True
                break
        if(result == False):
            print("Goldbach's conjecture is wrong.")
