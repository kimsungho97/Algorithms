n, k = list(map(int, input().split()))
arr = [i+1 for i in range(n)]

result = []
record = {}
record[0] = 1
for i in range(1, n):
    record[i] = (i+1)
record[n] = 1

prev = None
current = 0

for _ in range(n):
    for i in range(k):
        prev = current
        current = record[current]
    result.append(str(current))
    record[prev] = record[current]


print("<"+", ".join(result)+">")
