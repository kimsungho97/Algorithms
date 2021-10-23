n, m = list(map(int, input().split()))


temp = 1
count2 = 0
count5 = 0
for i in range(n, n-m-1, -1):
    temp *= i

while(temp % 10 != 0):
    temp = temp//10
    count2 += 1
    count5 += 1

while(temp % 2 != 0):
    temp = temp//2
    count2 += 1

while(temp % 5 != 0):
    temp = temp//5
    count5 += 1

temp = 1
for i in range(2, m+1):
    temp *= i

while(temp % 10 != 0):
    temp = temp//10
    count2 -= 1
    count5 -= 1

while(temp % 2 != 0):
    temp = temp//2
    count2 -= 1

while(temp % 5 != 0):
    temp = temp//5
    count5 -= 1


print(min(count2, count5))
