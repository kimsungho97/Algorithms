line = input()
count = 0
result = 0
isRazer = False

for c in range(len(line)):
    if(isRazer):
        isRazer = False
        continue

    if(line[c] == '('):
        if(line[c+1] == ')'):
            result += count
            isRazer = True
        else:
            count += 1
    elif(line[c] == ')'):
        result += 1
        count -= 1


print(result)
