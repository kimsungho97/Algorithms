'''n = int(input())

assigned = {}
operand = ['*', '+', '/', '-']
stack = []
line = input()

for i in range(len(line)):
    if(line[i] in operand):
        continue
    elif(line[i] in list(assigned.keys())):
        continue
    else:
        assigned[line[i]] = int(input())

operator = list(assigned.keys())

for c in line:
    if c in operand:
        b = stack.pop()
        a = stack.pop()
        if(c == '*'):
            stack.append(a*b)
        elif(c == '+'):
            stack.append(a+b)
        elif(c == '/'):
            stack.append(a/b)
        elif(c == '-'):
            stack.append(a-b)
    else:
        stack.append(assigned[c])

print('{:.2f}'.format(stack.pop()))
print(f'{stack.pop():.2f}')'''
print(r'\t')

print('\\t')
