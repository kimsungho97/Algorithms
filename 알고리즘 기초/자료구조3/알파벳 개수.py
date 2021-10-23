line = input()

result = [0 for i in range(ord('a'), ord('z')+1)]

for c in line:
    result[ord(c)-ord('a')] += 1

print(' '.join(list(map(str, result))))
