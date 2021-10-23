line = input()

result = [-1 for i in range(ord('a'), ord('z')+1)]

for c in range(len(line)):
    index = ord(line[c])-ord('a')
    if(result[index] == -1):
        result[index] = c

print(' '.join(list(map(str, result))))
