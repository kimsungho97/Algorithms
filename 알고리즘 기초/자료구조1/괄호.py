n = int(input())

lines = [input() for i in range(n)]


def check(line):
    stack = []
    for i in line:
        if(i == '('):
            stack.append(i)
        if(i == ')'):
            if(len(stack) == 0):
                return 'NO'
            if(stack.pop() != '('):
                return "NO"
    if(len(stack) != 0):
        return "NO"
    return "YES"


for i in lines:
    print(check(i))
