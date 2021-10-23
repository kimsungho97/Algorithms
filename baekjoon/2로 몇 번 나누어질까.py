# https://www.acmicpc.net/problem/1407
import math

a, b = list(map(int, input().split()))
numbers = []
k = 1
while k <= b:
    numbers.append(k)
    k *= 2


result = b-a+1
answers = []
for num in range(len(numbers)):
    if len(numbers) - 1 == num:
        break
    else:

        result += (math.floor(float(b) /
                   numbers[num+1]) - math.ceil(float(a)/numbers[num+1])+1) * numbers[num]

# print(answers)
# print(numbers)
print(result)
