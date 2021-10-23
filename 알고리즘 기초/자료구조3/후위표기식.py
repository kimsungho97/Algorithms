import sys

priority = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    ')': 3,
    '(': 3
}

resultStack = []
operatorStack = []
line = sys.stdin.readline().strip()


for c in line:
    #print(c, resultStack, operatorStack)
    if(priority.get(c) != None):  # 연산자임
        if(len(operatorStack) == 0):
            operatorStack.append(c)
        elif(c == '('):
            operatorStack.append(c)
        elif(c == ')'):
            while(len(operatorStack) > 0):
                temp = operatorStack.pop()
                if(temp == '('):
                    break
                else:
                    resultStack.append(temp)
        elif(operatorStack[-1] != "(" and priority[c] <= priority[operatorStack[-1]]):
            while(len(operatorStack) > 0):
                temp = operatorStack.pop()
                if(priority[c] > priority[temp]):
                    operatorStack.append(temp)
                    break
                resultStack.append(temp)
            operatorStack.append(c)
        else:
            operatorStack.append(c)
    elif(c.isalpha()):
        resultStack.append(c)

while(len(operatorStack) > 0):
    resultStack.append(operatorStack.pop())

answer = ''.join(resultStack)
answer = answer.replace("(", "")
answer = answer.replace(")", "")
print(answer)
