n, m = list(map(int, input().split()))

count = {}

for i in range(n):
    info = input()
    if count.get(info) == None:
        count[info] = 1
    else:
        count[info] += 1

result = 0

for i in count.values():
    result += int(i / m)
    if i % m != 0:
        result += 1

print(result)
