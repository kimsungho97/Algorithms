import sys


n = int(input())
stack = []
for i in range(n):
    cmd = sys.stdin.readline().strip()
    num = 0
    if(len(cmd.split(' ')) != 1):
        cmd, num = cmd.split(' ')
        num = int(num)

    if(cmd == 'push'):
        stack.append(num)
    elif(cmd == 'top'):
        if(len(stack) == 0):
            print(-1)
        else:
            print(stack[-1])
    elif(cmd == 'size'):
        print(len(stack))
    elif(cmd == 'pop'):
        if(len(stack) == 0):
            print(-1)
        else:
            print(stack.pop())
    elif(cmd == 'empty'):
        if(len(stack) == 0):
            print(1)
        else:
            print(0)
