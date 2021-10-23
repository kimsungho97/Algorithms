def reversing(word):
    result = ''
    for c in word:
        result = c+result
    return result


n = int(input())


lines = [input().split(' ') for i in range(n)]
for i in range(len(lines)):
    for j in range(len(lines[i])):
        lines[i][j] = reversing(lines[i][j])

for i in lines:
    print(' '.join(i))
