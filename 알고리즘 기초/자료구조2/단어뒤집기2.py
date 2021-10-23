line = input()

result = ''
stack = []
c = 0
while(c < len(line)):
    if(line[c] == '<'):
        for i in range(len(stack)):
            result += stack.pop()
        while(line[c] != '>'):
            result += line[c]
            c += 1
        result += line[c]
    elif(line[c] == ' '):
        for i in range(len(stack)):
            result += stack.pop()
        result += ' '
    else:
        stack.append(line[c])
    c += 1
for i in range(len(stack)):
    result += stack.pop()

print(result)
