n = int(input())

if(n <= 3):
    print(0)
else:
    result = 1
    for i in range(2, n+1):
        result *= i

    temp = list(str(result))
    temp.reverse()
    count = 0
    for i in temp:
        if(i == "0"):
            count += 1
        else:
            break
    print(count)
