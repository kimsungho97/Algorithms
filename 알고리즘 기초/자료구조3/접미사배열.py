line = input()

lines = []
for i in range(len(line)):
    lines.append(line[i:])

print('\n'.join(sorted(lines)))
