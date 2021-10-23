# https://www.acmicpc.net/problem/1132


n = int(input())
words = []
priority = {}
is_zero = {}
for i in range(n):
    words.append(input())

for w in words:
    temp = list(w)
    for alpha in range(len(temp)):
        if (alpha == 0):
            is_zero[temp[alpha]] = True
        if priority.get(temp[alpha]) == None:
            priority[temp[alpha]] = 10 ** (len(temp) - alpha)
        else:
            priority[temp[alpha]] += 10 ** (len(temp) - alpha)

numbers = [i for i in range(10-len(priority.keys()), 10)]


priority = list(priority.items())
priority.sort(reverse=False, key=lambda x: x[1])

matching = {}

for i in priority:
    if is_zero.get(i[0]) != None and numbers[0] == 0:
        matching[i[0]] = numbers[1]
        numbers.remove(numbers[1])
    else:
        matching[i[0]] = numbers[0]
        del numbers[0]


result = 0

for w in words:
    temp = list(w)
    for i in range(len(temp)):
        result += matching[temp[i]] * (10 ** (len(temp) - i - 1))
print(result)
