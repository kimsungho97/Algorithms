# https://www.acmicpc.net/problem/1011

n = int(input())
testcases = []
answer = []

for i in range(n):
    testcases.append(list(map(int, input().split())))

for i in testcases:
    distance = i[1] - i[0]
    total = 0
    k = 0
    count = 0
    while total < distance:
        if count % 2 == 1:
            total += k
            count += 1
        else:
            k += 1
            total += k
            count += 1
    #print(total, k)
    answer.append(count)


for i in answer:
    print(i)
